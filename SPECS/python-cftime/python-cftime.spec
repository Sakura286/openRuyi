# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname cftime

Name:           python-%{srcname}
Version:        1.6.5
Release:        %autorelease
Summary:        Time-handling functionality from netcdf4-python
License:        MIT
URL:            https://github.com/Unidata/cftime
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/c/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  gcc
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Time-handling functionality from netcdf4-python.

%generate_buildrequires
%pyproject_buildrequires

%check
%pyproject_check_import
%pytest

%files -f %{pyproject_files}
%doc README.md

%changelog
%{?autochangelog}
