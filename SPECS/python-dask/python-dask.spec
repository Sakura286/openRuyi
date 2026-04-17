# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# TODO: build cupy on openRuyi
%bcond cupy 0
# TODO: build scikit-image on openRuyi
%bcond skimage 0
# TODO: scipy on oR has no module named sparse, weird
%bcond sparse 0

%bcond test 0

%global srcname dask

Name:           python-%{srcname}
Version:        2026.3.0
Release:        %autorelease
Summary:        Parallel PyData with Task Scheduling
License:        BSD-3-Clause
URL:            https://github.com/dask/dask
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/d/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(scipy)
BuildRequires:  python3dist(xarray)
%{?with_cupy:BuildRequires:  python3dist(cupy)}
%{?with_skimage:BuildRequires:  python3dist(scikit-image)}

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Dask is a flexible parallel computing library for analytics.

%prep -a
sed -i -e 's|setuptools-scm>=9|setuptools-scm|' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%check
# Some test deps are not satisfied on openRuyi
%if %{with test}
%{pyproject_check_import %{!?with_cupy:-e 'dask.array.tests.test_cupy*'} \
                         %{!?with_skimage:-e 'dask.array.tests.test_image'} \
                         %{!?with_sparse:-e 'dask.array.tests.test_sparse'}}
%pytest
%endif

%files -f %{pyproject_files}
%license dask/array/NUMPY_LICENSE.txt
%doc README.rst
%{_bindir}/dask

%changelog
%{?autochangelog}
