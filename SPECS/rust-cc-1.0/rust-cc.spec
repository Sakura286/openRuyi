# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cc
%global full_version 1.2.62
%global pkgname cc-1.0

Name:           rust-cc-1.0
Version:        1.2.62
Release:        %autorelease
Summary:        Rust crate "cc"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-lang/cc-rs
#!RemoteAsset:  sha256:a1dce859f0832a7d088c4f1119888ab94ef4b5d6795d1ce05afb7fe159d79f98
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(find-msvc-tools-0.1/default) >= 0.1.9
Requires:       crate(shlex-1.0/default) >= 1.3.0
Provides:       crate(cc) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/jobserver)

%description
Source code for takopackized Rust crate "cc"

%package     -n %{name}+parallel
Summary:        Build-time dependency for Cargo build scripts to assist in invoking the native C compiler to compile native C code into a static archive to be linked into Rust code - feature "parallel"
Requires:       crate(%{pkgname})
Requires:       crate(jobserver-0.1) >= 0.1.34
Requires:       crate(libc-0.2) >= 0.2.186
Provides:       crate(%{pkgname}/parallel)

%description -n %{name}+parallel
This metapackage enables feature "parallel" for the Rust cc crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
