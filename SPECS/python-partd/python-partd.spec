# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# TODO: zmq is an optional requirement of partd
# used in some distributed environment
%bcond zmq 0

%global srcname partd

Name:           python-%{srcname}
Version:        1.4.2
Release:        %autorelease
Summary:        Appendable key-value storage
License:        BSD-3-Clause
URL:            https://github.com/dask/partd
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# TODO: temporary fix for packaging
Patch0:         2001-Fix-serialization-of-Pandas-3.x-extension-array-dtype.patch

BuildOption(install):  %{srcname}

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pandas)
BuildRequires:  python3dist(pytest)
%if %{with zmq}
BuildRequires:  python3dist(zmq)
%endif
BuildRequires:  systemd-resolved

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Key-value byte store with appendable values: Partd stores key-value pairs.
Values are raw bytes. We append on old values. Partd excels at shuffling
operations.

%generate_buildrequires
%pyproject_buildrequires

%check
%pyproject_check_import %{!?with_zmq:-e partd.zmq}
%pytest

%files -f %{pyproject_files}
%doc README.rst

%changelog
%{?autochangelog}
