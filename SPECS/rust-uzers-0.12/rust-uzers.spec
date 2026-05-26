# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name uzers
%global full_version 0.12.2
%global pkgname uzers-0.12

Name:           rust-uzers-0.12
Version:        0.12.2
Release:        %autorelease
Summary:        Rust crate "uzers"
License:        MIT
URL:            https://github.com/rustadopt/uzers-rs
#!RemoteAsset:  sha256:0b8275fb1afee25b4111d2dc8b5c505dbbc4afd0b990cb96deb2d88bff8be18d
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libc-0.2/default) >= 0.2.186
Provides:       crate(uzers) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/cache)
Provides:       crate(%{pkgname}/mock)
Provides:       crate(%{pkgname}/test-integration)

%description
Source code for takopackized Rust crate "uzers"

%package     -n %{name}+default
Summary:        Continuation of users, a library for accessing Unix users and groups - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/cache)
Requires:       crate(%{pkgname}/logging)
Requires:       crate(%{pkgname}/mock)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust uzers crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        Continuation of users, a library for accessing Unix users and groups - feature "log" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(log-0.4) >= 0.4.29
Provides:       crate(%{pkgname}/log)
Provides:       crate(%{pkgname}/logging)

%description -n %{name}+log
This metapackage enables feature "log" for the Rust uzers crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "logging" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
