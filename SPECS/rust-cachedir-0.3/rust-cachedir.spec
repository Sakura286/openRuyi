# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cachedir
%global full_version 0.3.1
%global pkgname cachedir-0.3

Name:           rust-cachedir-0.3
Version:        0.3.1
Release:        %autorelease
Summary:        Rust crate "cachedir"
License:        MIT
URL:            https://github.com/jstasiak/cachedir
#!RemoteAsset:  sha256:4703f3937077db8fa35bee3c8789343c1aec2585f0146f09d658d4ccc0e8d873
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(tempfile-3.0/default) >= 3.27.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "cachedir"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
