# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname pooch

Name:           python-%{srcname}
Version:        1.9.0
Release:        %autorelease
Summary:        A friend to fetch your data files
License:        BSD-3-Clause
URL:            https://github.com/fatiando/pooch
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Pooch manages your Python library's sample data files: 
it automatically downloads and stores them in a local directory, 
with support for versioning and corruption checks.

%generate_buildrequires
%pyproject_buildrequires

%check
# some checks guarded with '@pytest.mark.network',
# some checks need fixture from pytest-ftpserver/httpserver, we don't have them
%pytest -vv -rs -m 'not network' \
    -k 'not test_check_availability_on_ftp and not TestZenodoAPISupport'

%files -f %{pyproject_files}
%license LICENSE.txt
%doc README.md

%changelog
%{?autochangelog}
