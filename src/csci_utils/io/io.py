from contextlib import contextmanager
import os
import io
import tempfile
from atomicwrites import atomic_write as _backend_writer, AtomicWriter


class SuffixWriter(AtomicWriter):
    """Subclass of AtomicWriter that overrides get_fileobject
    """
    def get_fileobject(self, suffix="", dir=None, **kwargs):
        """ Overrides method of AtomicWriter which add the original file extension to the temporary file.
        :param suffix: String to append to end of the temporary file name.
        :param dir: Directory where the file will be written
        :param kwargs: other optional arguments for opening a file.
        :return: opened file like object
        """

        # Preserve the file ext by locating the first dot
        index = self._path.find(".")

        # No ext dot found, raise a TypeError.
        if index == -1:
            raise TypeError("The provided file path doesn't not have a required file extension.")

        # Get the extension
        ext = self._path[index:]

        '''Return the temporary file to use.'''
        if dir is None:
            dir = os.path.normpath(os.path.dirname(self._path))

        # Add the original file extension as the suffix to preserve the original ext.
        descriptor, name = tempfile.mkstemp(suffix='~' + ext, prefix=tempfile.template, dir=dir)

        # io.open() will take either the descriptor or the name, but we need
        # the name later for commit()/replace_atomic() and couldn't find a way
        # to get the filename from the descriptor.
        os.close(descriptor)
        kwargs['mode'] = self._mode
        kwargs['file'] = name
        return io.open(**kwargs)

@contextmanager
def atomic_write(file, as_file=True, new_default='asdf', **kwargs):

    # Override atomic_write of atomicwrites.
    with _backend_writer(file, writer_cls=SuffixWriter, **kwargs) as f:

        # Logic to yield a path to the temporary file if as_file is False.
        if not as_file:
            # Convert an os.Pathlike object to a path str if needed.
            file = os.fspath(file)
            yield file

        # Logic to yield a file like object.
        else:
            yield f
