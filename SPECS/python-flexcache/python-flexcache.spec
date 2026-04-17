# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname flexcache

Name:           python-%{srcname}
Version:        0.3
Release:        %autorelease
Summary:        Cache on disk the result of expensive calculations
License:        BSD-3-Clause
URL:            https://github.com/hgrecco/flexcache
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

Patch0:         0001-Increase-the-value-of-FS_SLEEP-in-the-tests-fix-4.patch

BuildOption(install):  %{srcname}

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
A robust and extensible package to cache on disk the result of expensive
calculations.

%generate_buildrequires
%pyproject_buildrequires

%check
%pyproject_check_import
%pytest

%files -f %{pyproject_files}
%doc CHANGES README.rst

%changelog
%{?autochangelog}
