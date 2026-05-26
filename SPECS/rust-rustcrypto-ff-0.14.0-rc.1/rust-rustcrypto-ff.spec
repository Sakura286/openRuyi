# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rustcrypto-ff
%global full_version 0.14.0-rc.1
%global pkgname rustcrypto-ff-0.14.0-rc.1

Name:           rust-rustcrypto-ff-0.14.0-rc.1
Version:        0.14.0
Release:        %autorelease
Summary:        Rust crate "rustcrypto-ff"
License:        MIT/Apache-2.0
URL:            https://github.com/RustCrypto/ff
#!RemoteAsset:  sha256:fd2a8adb347447693cd2ba0d218c4b66c62da9b0a5672b17b981e4291ec65ff6
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rand-core-0.10) >= 0.10.1
Requires:       crate(subtle-2.0/i128) >= 2.6.1
Provides:       crate(rustcrypto-ff) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "rustcrypto-ff"

%package     -n %{name}+bits
Summary:        Building and interfacing with finite fields - feature "bits"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitvec)
Requires:       crate(rustcrypto-ff-derive-0.14.0-rc.0/bits) >= 0.14.0-rc.0
Provides:       crate(%{pkgname}/bits)

%description -n %{name}+bits
This metapackage enables feature "bits" for the Rust rustcrypto-ff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bitvec
Summary:        Building and interfacing with finite fields - feature "bitvec"
Requires:       crate(%{pkgname})
Requires:       crate(bitvec-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/bitvec)

%description -n %{name}+bitvec
This metapackage enables feature "bitvec" for the Rust rustcrypto-ff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+byteorder
Summary:        Building and interfacing with finite fields - feature "byteorder"
Requires:       crate(%{pkgname})
Requires:       crate(byteorder-1.0) >= 1.0.0
Provides:       crate(%{pkgname}/byteorder)

%description -n %{name}+byteorder
This metapackage enables feature "byteorder" for the Rust rustcrypto-ff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Building and interfacing with finite fields - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bits)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust rustcrypto-ff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+derive
Summary:        Building and interfacing with finite fields - feature "derive"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/byteorder)
Requires:       crate(%{pkgname}/ff-derive)
Provides:       crate(%{pkgname}/derive)

%description -n %{name}+derive
This metapackage enables feature "derive" for the Rust rustcrypto-ff crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ff-derive
Summary:        Building and interfacing with finite fields - feature "ff_derive"
Requires:       crate(%{pkgname})
Requires:       crate(rustcrypto-ff-derive-0.14.0-rc.0/default) >= 0.14.0-rc.0
Provides:       crate(%{pkgname}/ff-derive)

%description -n %{name}+ff-derive
This metapackage enables feature "ff_derive" for the Rust rustcrypto-ff crate, by pulling in any additional dependencies needed by that feature.

%install -a
if [ -d "%{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{version}" ]; then
    mv "%{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{version}" \
       "%{buildroot}%{_datadir}/cargo/registry/%{crate_name}-%{full_version}"
fi

%files
%{_datadir}/cargo/registry/%{crate_name}-%{full_version}/

%changelog
%autochangelog
