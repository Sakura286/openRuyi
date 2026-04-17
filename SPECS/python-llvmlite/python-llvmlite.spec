# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname llvmlite

# Bundled LLVM version (llvmlite only supports LLVM 20)
%global llvm_bundled_version 20.1.8

Name:           python-%{srcname}
Version:        0.47.0
Release:        %autorelease
Summary:        Lightweight LLVM Python binding for writing JIT compilers
License:        BSD-2-Clause AND Apache-2.0
URL:            http://llvmlite.pydata.org/
VCS:            git:https://github.com/numba/llvmlite
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/l/%{srcname}/%{srcname}-%{version}.tar.gz
#!RemoteAsset
Source1:        https://github.com/llvm/llvm-project/archive/refs/tags/llvmorg-%{llvm_bundled_version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  cmake
BuildRequires:  ninja
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)

Provides:       python3-%{srcname}
Provides:       bundled(llvm) = %{llvm_bundled_version}
%python_provide python3-%{srcname}

%description
llvmlite is a project originally tailored for Numba's needs, using the
following approach:

  • A small C wrapper around the parts of the LLVM C++ API we need that are not
    already exposed by the LLVM C API.
  • A ctypes Python wrapper around the C API.
  • A pure Python implementation of the subset of the LLVM IR builder that we
    need for Numba.

%package        doc
Summary:        Examples for python-llvmlite
BuildArch:      noarch

%description    doc
Examples for python-llvmlite

%prep
%autosetup -n %{srcname}-%{version} -a 1

# increase verbosity of tests to 2
sed -i 's/\(def run_tests.*verbosity=\)1/\12/' llvmlite/tests/__init__.py

%generate_buildrequires
%pyproject_buildrequires

%build
# Build bundled LLVM 20 (static libs only)
%global _llvm_prefix %{_builddir}/llvm-install

find %{_builddir} -maxdepth 3

%global _llvm_srcdir %{_builddir}/%{srcname}-%{version}/llvm-project-llvmorg-%{llvm_bundled_version}

pushd %{_llvm_srcdir}

mkdir -p build-llvm
cd build-llvm

# Just use static lib for temporarily, not for packaging,
# so %%cmake not used here
cmake -S ../llvm \
    -DCMAKE_INSTALL_PREFIX=%{_llvm_prefix} \
    -DCMAKE_BUILD_TYPE=Release \
    -DLLVM_ENABLE_RTTI=OFF \
    -DLLVM_ENABLE_ASSERTIONS=ON \
    -DLLVM_ENABLE_TERMINFO=OFF \
    -DLLVM_ENABLE_LIBEDIT=OFF \
    -DLLVM_ENABLE_LIBXML2=OFF \
    -DLLVM_ENABLE_FFI=OFF \
    -DLLVM_ENABLE_Z3_SOLVER=OFF \
    -DLLVM_ENABLE_ZLIB=ON \
    -DLLVM_ENABLE_ZSTD=ON \
    -DLLVM_BUILD_LLVM_DYLIB=OFF \
    -DLLVM_LINK_LLVM_DYLIB=OFF \
    -DLLVM_INCLUDE_BENCHMARKS=OFF \
    -DLLVM_INCLUDE_DOCS=OFF \
    -DLLVM_INCLUDE_EXAMPLES=OFF \
    -DLLVM_INCLUDE_TESTS=OFF \
    -DLLVM_INCLUDE_GO_TESTS=OFF \
    -DLLVM_INCLUDE_UTILS=OFF \
    -DLLVM_OPTIMIZED_TABLEGEN=ON \
    -DLLVM_TARGETS_TO_BUILD="host" \
    -GNinja
(while true; do echo "[heartbeat] $(date) - build still running..."; sleep 300; done) &
HEARTBEAT_PID=$!
cmake --build . -j%{_smp_build_ncpus}
kill $HEARTBEAT_PID 2>/dev/null || true
cmake --install . --prefix %{_llvm_prefix}

popd

# Build llvmlite against bundled LLVM 20
# Point CMake at bundled LLVM 20's cmake config
export CMAKE_PREFIX_PATH="%{_llvm_prefix}/lib/cmake/llvm:%{_llvm_prefix}/lib64/cmake/llvm"
# Static link (default, do NOT set LLVMLITE_SHARED=1 since we don't install libLLVM.so)
unset LLVMLITE_SHARED
export VERBOSE=1
%pyproject_wheel

%check
%ifarch riscv64
# Disable JIT tests on riscv64 since that feature is not supported
# upstream yet. See:
# https://github.com/numba/llvmlite/issues/923
# https://github.com/felixonmars/archriscv-packages/blob/master/python-llvmlite/riscv64.patch
export PYTEST_ADDOPTS="\
        --deselect llvmlite/tests/test_binding.py::TestMCJit \
        --deselect llvmlite/tests/test_binding.py::TestGlobalConstructors \
        --deselect llvmlite/tests/test_binding.py::TestObjectFile::test_add_object_file \
        --deselect llvmlite/tests/test_binding.py::TestOrcLLJIT \
        --deselect llvmlite/tests/test_binding.py::TestDylib::test_bad_library"
%endif
%pytest -vv llvmlite/tests

%files -f %{pyproject_files}
%doc README.rst

%files doc
%license LICENSE LICENSE.thirdparty
%doc examples/

%changelog
%{?autochangelog}
