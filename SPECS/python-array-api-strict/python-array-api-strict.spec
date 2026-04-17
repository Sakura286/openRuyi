# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname array-api-strict
%global modname array_api_strict

Name:           python-%{srcname}
# 20260320: latest version is 2.5, use array api version 2025.12
# https://github.com/data-apis/array-api-strict/commit/cc0a86c6
# But hypothesis 6.148.6 is used, which only support up to '2024.12'
# TODO: upgrade this package once hopothesis is bumped to 6.151.9
# https://github.com/HypothesisWorks/hypothesis/commit/edb6701c
Version:        2.4
Release:        %autorelease
Summary:        Strict implementation of the Python array API
License:        BSD-3-Clause
URL:            https://github.com/data-apis/array-api-strict
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/a/%{modname}/%{modname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# Fix test - test_scalars & test_operators
# The patch will be included in 2.5 version
Patch0:         0001-replace-suppress_warnings-with-stdlib.patch

BuildOption(install):  %{modname}

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(hypothesis)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
array_api_strict is a strict, minimal implementation of the Python array API.

The purpose of array-api-strict is to provide an implementation of the array
API for consuming libraries to test against so they can be completely sure
their usage of the array API is portable.

It is not intended to be used by end-users. End-users of the array API should
just use their favorite array library (NumPy, CuPy, PyTorch, etc.) as usual. It
is also not intended to be used as a dependency by consuming libraries.
Consuming library code should use the array-api-compat package to support the
array API. Rather, it is intended to be used in the test suites of consuming
libraries to test their array API usage.

%prep -a
# on oR, setuptools is too new, setuptools_scm is too old
sed -i -e 's|"setuptools >= 61.0,<=75", "setuptools_scm>8"|"setuptools", "setuptools_scm"|' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%check
%pyproject_check_import
%ifarch riscv64
%pytest -rs --hypothesis-suppress-health-check=too_slow
%else
%pytest -rs
%endif


%files -f %{pyproject_files}
%doc README.md

%changelog
%{?autochangelog}
