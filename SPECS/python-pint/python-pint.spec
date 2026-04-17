# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# TODO: pint and xarray requires each other
# openRuyi misses some buildreq
%bcond bootstrap 1

%global srcname pint

Name:           python-%{srcname}
Version:        0.25.3
Release:        %autorelease
Summary:        Physical quantities module
License:        BSD-3-Clause
URL:            https://github.com/hgrecco/pint
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(scipy)
%if %{without bootstrap}
BuildRequires:  python3dist(xarray)
BuildRequires:  python3dist(babel)
BuildRequires:  python3dist(dask)
BuildRequires:  python3dist(sparse)
BuildRequires:  python3dist(matplotlib)
BuildRequires:  python3dist(uncertainties)
%endif


Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Pint is a Python package to define, operate and manipulate physical quantities:
the product of a numerical value and a unit of measurement. It allows
arithmetic operations between them and conversions from and to different units.

It is distributed with a comprehensive list of physical units, prefixes and
constants.

%generate_buildrequires
%pyproject_buildrequires

%check
# pint.matplotlib                       - no matplotlib
# pint.testsuite.test_matplotlib        - no matplotlib
# pint.testsuite.test_compat_downcase   - no sparse
# pint.testsuite.test_compat_upcast     - no dask
# pint.testsuite.test_dask              - no dask
%{pyproject_check_import %{?with_bootstrap: \
    -e 'pint.testsuite.test_matplotlib' \
    -e 'pint.matplotlib' \
    -e 'pint.testsuite.test_compat_upcast' \
    -e 'pint.testsuite.test_compat_downcast' \
    -e 'pint.testsuite.test_dask'}}
# TODO
# no pytest-benchmark on openRuyi
%pytest -rs --ignore=pint/testsuite/benchmarks

%files -f %{pyproject_files}
%{_bindir}/pint-convert

%changelog
%{?autochangelog}
