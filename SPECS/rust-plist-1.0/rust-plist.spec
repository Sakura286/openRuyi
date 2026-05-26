# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name plist
%global full_version 1.9.0
%global pkgname plist-1.0

Name:           rust-plist-1.0
Version:        1.9.0
Release:        %autorelease
Summary:        Rust crate "plist"
License:        MIT
URL:            https://github.com/ebarnard/rust-plist/
#!RemoteAsset:  sha256:092791278e026273c1b65bbdcfbba3a300f2994c896bd01ab01da613c29c46f1
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(base64-0.22/default) >= 0.22.1
Requires:       crate(indexmap-2.14.0/default) >= 2.14.0
Requires:       crate(quick-xml-0.39/default) >= 0.39.4
Requires:       crate(time-0.3/default) >= 0.3.47
Requires:       crate(time-0.3/formatting) >= 0.3.47
Requires:       crate(time-0.3/parsing) >= 0.3.47
Provides:       crate(plist) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/enable-unstable-features-that-may-break-with-minor-version-bumps)

%description
Supports Serde serialization.
Source code for takopackized Rust crate "plist"

%package     -n %{name}+serde
Summary:        Rusty plist parser - feature "serde" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(serde-1.0/default) >= 1.0.228
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
Supports Serde serialization.
This metapackage enables feature "serde" for the Rust plist crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
