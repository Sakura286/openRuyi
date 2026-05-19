# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name attribute-derive-macro
%global full_version 0.10.3
%global pkgname attribute-derive-macro-0.10

Name:           rust-attribute-derive-macro-0.10
Version:        0.10.3
Release:        %autorelease
Summary:        Rust crate "attribute-derive-macro"
License:        MIT
URL:            https://github.com/ModProg/attribute-derive
#!RemoteAsset:  sha256:463b53ad0fd5b460af4b1915fe045ff4d946d025fb6c4dc3337752eaa980f71b
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(collection-literals-1.0/default) >= 1.0.2
Requires:       crate(interpolator-0.5/default) >= 0.5.0
Requires:       crate(interpolator-0.5/iter) >= 0.5.0
Requires:       crate(manyhow-0.11/default) >= 0.11.4
Requires:       crate(proc-macro-utils-0.10/default) >= 0.10.0
Requires:       crate(proc-macro2-1.0/default) >= 1.0.106
Requires:       crate(quote-1.0/default) >= 1.0.45
Requires:       crate(quote-use-0.8/default) >= 0.8.4
Requires:       crate(syn-2.0/default) >= 2.0.117
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "attribute-derive-macro"

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
