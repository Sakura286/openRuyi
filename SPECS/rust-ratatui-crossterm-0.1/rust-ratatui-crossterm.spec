# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ratatui-crossterm
%global full_version 0.1.0
%global pkgname ratatui-crossterm-0.1

Name:           rust-ratatui-crossterm-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "ratatui-crossterm"
License:        MIT
URL:            https://ratatui.rs
#!RemoteAsset:  sha256:577c9b9f652b4c121fb25c6a391dd06406d3b092ba68827e6d2f09550edc54b3
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1.0/default) >= 1.0.4
Requires:       crate(instability-0.3/default) >= 0.3.12
Requires:       crate(ratatui-core-0.1/default) >= 0.1.0
Provides:       crate(ratatui-crossterm) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/unstable)
Provides:       crate(%{pkgname}/unstable-backend-writer)

%description
Source code for takopackized Rust crate "ratatui-crossterm"

%package     -n %{name}+crossterm-0-28
Summary:        Crossterm backend for the Ratatui Terminal UI library - feature "crossterm_0_28"
Requires:       crate(%{pkgname})
Requires:       crate(crossterm-0.28/default) >= 0.28.1
Provides:       crate(%{pkgname}/crossterm-0-28)

%description -n %{name}+crossterm-0-28
This metapackage enables feature "crossterm_0_28" for the Rust ratatui-crossterm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+crossterm-0-29
Summary:        Crossterm backend for the Ratatui Terminal UI library - feature "crossterm_0_29"
Requires:       crate(%{pkgname})
Requires:       crate(crossterm-0.29/default) >= 0.29.0
Provides:       crate(%{pkgname}/crossterm-0-29)

%description -n %{name}+crossterm-0-29
This metapackage enables feature "crossterm_0_29" for the Rust ratatui-crossterm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Crossterm backend for the Ratatui Terminal UI library - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/crossterm-0-29)
Requires:       crate(%{pkgname}/underline-color)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust ratatui-crossterm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+document-features
Summary:        Crossterm backend for the Ratatui Terminal UI library - feature "document-features"
Requires:       crate(%{pkgname})
Requires:       crate(document-features-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/document-features)

%description -n %{name}+document-features
This metapackage enables feature "document-features" for the Rust ratatui-crossterm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+scrolling-regions
Summary:        Crossterm backend for the Ratatui Terminal UI library - feature "scrolling-regions"
Requires:       crate(%{pkgname})
Requires:       crate(ratatui-core-0.1/scrolling-regions) >= 0.1.0
Provides:       crate(%{pkgname}/scrolling-regions)

%description -n %{name}+scrolling-regions
This metapackage enables feature "scrolling-regions" for the Rust ratatui-crossterm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Crossterm backend for the Ratatui Terminal UI library - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(crossterm-0.29/serde) >= 0.29.0
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust ratatui-crossterm crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+underline-color
Summary:        Crossterm backend for the Ratatui Terminal UI library - feature "underline-color"
Requires:       crate(%{pkgname})
Requires:       crate(ratatui-core-0.1/underline-color) >= 0.1.0
Provides:       crate(%{pkgname}/underline-color)

%description -n %{name}+underline-color
This metapackage enables feature "underline-color" for the Rust ratatui-crossterm crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
