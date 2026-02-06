project('JFNK-Hookstep', ['c', 'fortran'], version: '0.1.0')

py = import('python').find_installation()
py_install_dir = py.get_install_dir()

# Python import package name (must be a valid identifier)
pkgname = 'jfnk_hookstep'

# Install pure-Python sources
install_subdir('src/' + pkgname, install_dir: py_install_dir)

# Install location for extension inside package
pkgdir = py_install_dir / pkgname

python_exe = py.full_path()
f2py_cmd = [python_exe, '-m', 'numpy.f2py']

ext_suffix = run_command(
  python_exe, ['-c', 'import sysconfig; print(sysconfig.get_config_var("EXT_SUFFIX") or "")'],
  check: true
).stdout().strip()

ext_modname = '_fortran_backend'
ext_filename = ext_modname + ext_suffix

# Try OpenBLAS via pkg-config first, then fall back to -llapack -lblas
openblas = dependency('openblas', required: false)

link_args = []
if openblas.found()
  link_args = openblas.get_link_args()
else
  # Works if reference BLAS/LAPACK development packages are installed
  link_args = ['-llapack', '-lblas']
endif

custom_target(
  ext_modname + '_ext',
  input: [
    'JFNK-Hookstep.pyf',
    '../Fortran90/NewtonHook.f90',
    '../Fortran90/GMRESm.f90',
  ],
  output: ext_filename,
  command: f2py_cmd + [
    '-c',
    '-m', ext_modname,
    '@INPUT@',
    '--build-dir', '@OUTDIR@/f2py',
    ] + link_args,
  install: true,
  install_dir: pkgdir,
)
