# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname flexparser

Name:           python-%{srcname}
Version:        0.4
Release:        %autorelease
Summary:        Parsing made fun … using typing
License:        BSD-3-Clause
URL:            https://github.com/hgrecco/flexparser
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
The idea is quite simple. You write a class for every type of content (called
here ParsedStatement) you need to parse. Each class should have a from_string
constructor. We used extensively the typing module to make the output structure
easy to use and less error prone.

%generate_buildrequires
%pyproject_buildrequires

%check
%pyproject_check_import
%pytest

%files -f %{pyproject_files}
%doc CHANGES README.rst

%changelog
%{?autochangelog}
