# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name get-size-derive2
%global full_version 0.8.0
%global pkgname get-size-derive2-0.8

Name:           rust-get-size-derive2-0.8
Version:        0.8.0
Release:        %autorelease
Summary:        Rust crate "get-size-derive2"
License:        MIT OR Apache-2.0
URL:            https://github.com/bircni/get-size2/tree/main/crates/get-size-derive2
#!RemoteAsset:  sha256:dfd774e8175d3adb09c1742cb4697fb08490607fc02acfaa3b66b88254239d1d
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(attribute-derive-0.10/default) >= 0.10.3
Requires:       crate(quote-1.0/default) >= 1.0.45
Requires:       crate(syn-2.0/default) >= 2.0.117
Requires:       crate(syn-2.0/derive) >= 2.0.117
Requires:       crate(syn-2.0/parsing) >= 2.0.117
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "get-size-derive2"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
