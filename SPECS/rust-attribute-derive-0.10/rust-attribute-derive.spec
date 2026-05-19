# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name attribute-derive
%global full_version 0.10.3
%global pkgname attribute-derive-0.10

Name:           rust-attribute-derive-0.10
Version:        0.10.3
Release:        %autorelease
Summary:        Rust crate "attribute-derive"
License:        MIT OR Apache-2.0
URL:            https://github.com/ModProg/attribute-derive
#!RemoteAsset:  sha256:0053e96dd3bec5b4879c23a138d6ef26f2cb936c9cdc96274ac2b9ed44b5bb54
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(attribute-derive-macro-0.10/default) >= 0.10.3
Requires:       crate(derive-where-1.0/default) >= 1.6.0
Requires:       crate(manyhow-0.11/default) >= 0.11.4
Requires:       crate(proc-macro2-1.0/default) >= 1.0.106
Requires:       crate(quote-1.0/default) >= 1.0.45
Requires:       crate(syn-2.0/default) >= 2.0.117
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "attribute-derive"

%package     -n %{name}+syn-full
Summary:        Clap like parsing for attributes in proc-macros - feature "syn-full"
Requires:       crate(%{pkgname})
Requires:       crate(syn-2.0/full) >= 2.0.117
Provides:       crate(%{pkgname}/syn-full)

%description -n %{name}+syn-full
This metapackage enables feature "syn-full" for the Rust attribute-derive crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
