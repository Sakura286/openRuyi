# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# TODO: Enable check if JIT tests on riscv64 of llvmlite fixed
%bcond check 0

%global srcname numba

Name:           python-%{srcname}
Version:        0.65.0
Release:        %autorelease
Summary:        A Just-In-Time Compiler for Numerical Functions in Python
License:        BSD
URL:            https://numba.pydata.org/
VCS:            git:https://github.com/numba/numba
#!RemoteAsset
Source0:        https://github.com/numba/numba/archive/refs/tags/%{version}.tar.gz
# Source0:        https://files.pythonhosted.org/packages/source/n/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pytest)
# For test, 'numba.misc.gdb_print_extension' need this
BuildRequires:  gdb

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Numba is an open source, NumPy-aware optimizing compiler for Python sponsored
by Anaconda, Inc. It uses the LLVM compiler project to generate machine code
from Python syntax.

Numba can compile a large subset of numerically-focused Python, including many
NumPy functions. Additionally, Numba has support for automatic parallelization
of loops, generation of GPU-accelerated code, and creation of ufuncs and C
callbacks.

%generate_buildrequires
%pyproject_buildrequires

%check
%if %{with check}
# numba.cuda.*: no cuda and no graphic card on buildsystem
# numba.misc.gdb_print_extension: no
# numba.tests.pycc_distutils_usecase.*: these modules are dynamiclly generated during testing
%{pyproject_check_import \
    -e 'numba.cuda.*' \
    -e 'numba.misc.gdb_print_extension' \
    -e 'numba.testing.notebook' \
    -e 'numba.tests.pycc_distutils_usecase.*'}
# MCJIT on riscv64 have some issues with relocation
# https://github.com/numba/llvmlite/issues/923

cd %{_tmppath}
%pytest --pyargs numba -x --ignore=%{buildroot}%{python3_sitearch}/numba/cuda -svv
%endif

%files -f %{pyproject_files}
%license LICENSE
%doc README.rst
%{_bindir}/numba

%changelog
%{?autochangelog}
