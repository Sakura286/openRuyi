# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname locket

Name:           python-%{srcname}
Version:        1.0.0
Release:        %autorelease
Summary:        File-based locks for Python for Linux and Windows
License:        BSD-2-Clause
URL:            https://github.com/mwilliamson/locket.py
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/l/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  %{srcname}

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Locket implements a lock that can be used by multiple processes provided they
use the same path.

Locks largely behave as (non-reentrant) Lock instances from the threading
module in the standard library. Specifically, their behaviour is:

 * Locks are uniquely identified by the file being locked, both in the same
   process and across different processes.
 * Locks are either in a locked or unlocked state.
 * When the lock is unlocked, calling acquire() returns immediately and
   changes the lock state to locked.
 * When the lock is locked, calling acquire() will block until the lock state
   changes to unlocked, or until the timeout expires.
 * If a process holds a lock, any thread in that process can call release()
   to change the state to unlocked.
 * Behaviour of locks after fork is undefined.

%generate_buildrequires
%pyproject_buildrequires

%check
%pyproject_check_import
#TODO: this package use tox to test

%files -f %{pyproject_files}
%doc README.rst

%changelog
%{?autochangelog}
