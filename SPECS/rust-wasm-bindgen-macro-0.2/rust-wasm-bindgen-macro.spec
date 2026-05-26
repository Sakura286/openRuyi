# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name wasm-bindgen-macro
%global full_version 0.2.121
%global pkgname wasm-bindgen-macro-0.2

Name:           rust-wasm-bindgen-macro-0.2
Version:        0.2.121
Release:        %autorelease
Summary:        Rust crate "wasm-bindgen-macro"
License:        MIT OR Apache-2.0
URL:            https://wasm-bindgen.github.io/wasm-bindgen/
#!RemoteAsset:  sha256:8e68e6f4afd367a562002c05637acb8578ff2dea1943df76afb9e83d177c8578
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(quote-1.0/default) >= 1.0.45
Requires:       crate(wasm-bindgen-macro-support-0.2/default) >= 0.2.121
Provides:       crate(wasm-bindgen-macro) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "wasm-bindgen-macro"

%package     -n %{name}+strict-macro
Summary:        Definition of the `#[wasm_bindgen]` attribute, an internal dependency - feature "strict-macro"
Requires:       crate(%{pkgname})
Requires:       crate(wasm-bindgen-macro-support-0.2/strict-macro) >= 0.2.121
Provides:       crate(%{pkgname}/strict-macro)

%description -n %{name}+strict-macro
This metapackage enables feature "strict-macro" for the Rust wasm-bindgen-macro crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
