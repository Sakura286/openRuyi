# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name libfuzzer-sys
%global full_version 0.4.12
%global pkgname libfuzzer-sys-0.4

Name:           rust-libfuzzer-sys-0.4
Version:        0.4.12
Release:        %autorelease
Summary:        Rust crate "libfuzzer-sys"
License:        (MIT OR Apache-2.0) AND NCSA
URL:            https://github.com/rust-fuzz/libfuzzer
#!RemoteAsset:  sha256:f12a681b7dd8ce12bff52488013ba614b869148d54dd79836ab85aafdd53f08d
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(arbitrary-1.0/default) >= 1.4.2
Requires:       crate(cc-1.0/default) >= 1.2.62
Requires:       crate(cc-1.0/parallel) >= 1.2.62
Provides:       crate(libfuzzer-sys) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/link-libfuzzer)

%description
Source code for takopackized Rust crate "libfuzzer-sys"

%package     -n %{name}+arbitrary-derive
Summary:        Wrapper around LLVM's libFuzzer runtime - feature "arbitrary-derive"
Requires:       crate(%{pkgname})
Requires:       crate(arbitrary-1.0/derive) >= 1.4.2
Provides:       crate(%{pkgname}/arbitrary-derive)

%description -n %{name}+arbitrary-derive
This metapackage enables feature "arbitrary-derive" for the Rust libfuzzer-sys crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
