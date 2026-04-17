# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname librosa

Name:           python-%{srcname}
Version:        0.11.0
Release:        %autorelease
Summary:        A python package for music and audio analysis.
License:        ISC
URL:            https://librosa.org/
VCS:            git:https://github.com/librosa/librosa.git
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/l/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install): %{srcname}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
librosa is a python package for music and audio analysis. It provides the building
blocks necessary to create music information retrieval systems.

%generate_buildrequires
%pyproject_buildrequires

%check
# TODO: no matplotlib on openRuyi, 'librosa.display' cannot be imported
# TODO: on riscv64, 'librosa.core' generate LLVM ERROR: Unimplemented reloc type: 53
# TODO: no coverage on openRuyi, skip pytest

%files -f %{pyproject_files}
%license LICENSE.md
%doc README.md

%changelog
%{?autochangelog}
