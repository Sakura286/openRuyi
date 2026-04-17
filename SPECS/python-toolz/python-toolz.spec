# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname toolz

Name:           python-%{srcname}
Version:        1.1.0
Release:        %autorelease
Summary:        A functional standard library for Python
License:        BSD-3-Clause
URL:            https://github.com/pytoolz/toolz
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  toolz tlz

BuildRequires:  python3dist(pytest)
BuildRequires:  pkgconfig(python3)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
Toolz provides a set of utility functions for iterators, functions, and\
dictionaries. These functions interoperate well and form the building blocks\
of common data analytic operations. They extend the standard libraries\
itertools and functools and borrow heavily from the standard libraries of\
contemporary functional languages.

Toolz provides a suite of functions which have the following functional
virtues:

    Composable: They interoperate due to their use of core data structures.
    Pure: They don't change their inputs or rely on external state.
    Lazy: They don't run until absolutely necessary, allowing them to support
          large streaming data sets.

Toolz functions are pragmatic. They understand that most programmers have
deadlines.

    Low Tech: They're just functions, no syntax or magic tricks to learn
    Tuned: They're profiled and optimized
    Serializable: They support common solutions for parallel computing

This gives developers the power to write powerful programs to solve complex
problems with relatively simple code. This code can be easy to understand
without sacrificing performance. Toolz enables this approach, commonly
associated with functional programming, within a natural Pythonic style
suitable for most developers.

%prep -a
# this spec use source tarball from pypi
# test_has_version need setuptools-git-versioning to get version
# so overlay the version in pyproject.toml
sed -i -e 's|"setuptools-git-versioning >=2.0",||' \
       -e 's|dynamic = \["version"\]|version = "%{version}"|' \
       pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%check
# shakespeare test downloads a file
%pytest -v -k 'not test_shakespeare'

%files -f %{pyproject_files}
%license LICENSE.txt

%changelog
%{?autochangelog}
