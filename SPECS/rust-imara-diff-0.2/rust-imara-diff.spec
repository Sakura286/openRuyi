# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name imara-diff
%global full_version 0.2.0
%global pkgname imara-diff-0.2

Name:           rust-imara-diff-0.2
Version:        0.2.0
Release:        %autorelease
Summary:        Rust crate "imara-diff"
License:        Apache-2.0
URL:            https://github.com/pascalkuthe/imara-diff
#!RemoteAsset:  sha256:2f01d462f766df78ab820dd06f5eb700233c51f0f4c2e846520eaf4ba6aa5c5c
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(hashbrown-0.15/default-hasher) >= 0.15.5
Requires:       crate(hashbrown-0.15/inline-more) >= 0.15.5
Requires:       crate(memchr-2.0/default) >= 2.8.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/unified-diff)

%description
Source code for takopackized Rust crate "imara-diff"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
