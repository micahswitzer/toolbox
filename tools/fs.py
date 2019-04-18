__all__ = ['mount']
import ctypes, ctypes.util
from typing import Union
NoneStr = Union[str, None]

libc = ctypes.CDLL(ctypes.util.find_library('c'), use_errno=True)
libc.mount.argtypes = [ctypes.c_char_p, ctypes.c_char_p, \
    ctypes.c_char_p, ctypes.c_ulong, ctypes.c_char_p]

def nonestr_enc(string: NoneStr) -> Union[bytes, None]:
    return None if string is None else string.encode()

"""
mount some code yeah
"""
def mount(source: NoneStr, target: NoneStr, fstype: str, flags: int, data: NoneStr) -> int:
    """
    source: Source block device
    target: Target directory
    """
    return libc.mount(nonestr_enc(source), nonestr_enc(target), \
        nonestr_enc(fstype), flags, nonestr_enc(data))

def mount_wiz():
    source = input('Block device: ') or None
    target = input('Target directory: ') or None
    fstype = input('Filesystem type: ') or None
    data = input('Mount options: ') or None
    res = mount(source, target, fstype, 0, data)
    if res == 0: print('mount succeeded')
    else: print('mount failed with error code', res)

if __name__ == '__main__':
    mount_wiz()
