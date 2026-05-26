# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name litrs
%global full_version 1.0.0
%global pkgname litrs-1.0

Name:           rust-litrs-1.0
Version:        1.0.0
Release:        %autorelease
Summary:        Rust crate "litrs"
License:        MIT OR Apache-2.0
URL:            https://github.com/LukasKalbertodt/litrs
#!RemoteAsset:  sha256:11d3d7f243d5c5a8b9bb5d6dd2b1602c0cb0b9db1621bafc7ed66e35ff9fe092
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Provides:       crate(litrs) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
tokens in the Rust programming language representing fixed values). Particularly useful for proc macros, but can also be used outside of a proc-macro context.
Source code for takopackized Rust crate "litrs"

%package     -n %{name}+proc-macro2
Summary:        Parse and inspect Rust literals (i.e - feature "proc-macro2"
Requires:       crate(%{pkgname})
Requires:       crate(proc-macro2-1.0/default) >= 1.0.63
Provides:       crate(%{pkgname}/proc-macro2)

%description -n %{name}+proc-macro2
tokens in the Rust programming language representing fixed values). Particularly useful for proc macros, but can also be used outside of a proc-macro context.
This metapackage enables feature "proc-macro2" for the Rust litrs crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unicode-xid
Summary:        Parse and inspect Rust literals (i.e - feature "unicode-xid" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(unicode-xid-0.2/default) >= 0.2.4
Provides:       crate(%{pkgname}/check-suffix)
Provides:       crate(%{pkgname}/unicode-xid)

%description -n %{name}+unicode-xid
tokens in the Rust programming language representing fixed values). Particularly useful for proc macros, but can also be used outside of a proc-macro context.
This metapackage enables feature "unicode-xid" for the Rust litrs crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "check_suffix" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
