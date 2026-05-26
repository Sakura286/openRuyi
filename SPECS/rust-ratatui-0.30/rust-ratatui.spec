# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ratatui
%global full_version 0.30.0
%global pkgname ratatui-0.30

Name:           rust-ratatui-0.30
Version:        0.30.0
Release:        %autorelease
Summary:        Rust crate "ratatui"
License:        MIT
URL:            https://ratatui.rs
#!RemoteAsset:  sha256:d1ce67fb8ba4446454d1c8dbaeda0557ff5e94d39d5e5ed7f10a65eb4c8266bc
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(instability-0.3/default) >= 0.3.12
Requires:       crate(ratatui-core-0.1/default) >= 0.1.0
Requires:       crate(ratatui-widgets-0.3/default) >= 0.3.0
Provides:       crate(ratatui) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/unstable-widget-ref)

%description
Source code for takopackized Rust crate "ratatui"

%package     -n %{name}+crossterm
Summary:        Library that's all about cooking up terminal user interfaces - feature "crossterm"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/std)
Requires:       crate(ratatui-crossterm-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/crossterm)

%description -n %{name}+crossterm
This metapackage enables feature "crossterm" for the Rust ratatui crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+crossterm-0-28
Summary:        Library that's all about cooking up terminal user interfaces - feature "crossterm_0_28"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/crossterm)
Requires:       crate(ratatui-crossterm-0.1/crossterm-0-28) >= 0.1.0
Provides:       crate(%{pkgname}/crossterm-0-28)

%description -n %{name}+crossterm-0-28
This metapackage enables feature "crossterm_0_28" for the Rust ratatui crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+crossterm-0-29
Summary:        Library that's all about cooking up terminal user interfaces - feature "crossterm_0_29"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/crossterm)
Requires:       crate(ratatui-crossterm-0.1/crossterm-0-29) >= 0.1.0
Provides:       crate(%{pkgname}/crossterm-0-29)

%description -n %{name}+crossterm-0-29
This metapackage enables feature "crossterm_0_29" for the Rust ratatui crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Library that's all about cooking up terminal user interfaces - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/all-widgets)
Requires:       crate(%{pkgname}/crossterm)
Requires:       crate(%{pkgname}/layout-cache)
Requires:       crate(%{pkgname}/macros)
Requires:       crate(%{pkgname}/underline-color)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust ratatui crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+document-features
Summary:        Library that's all about cooking up terminal user interfaces - feature "document-features"
Requires:       crate(%{pkgname})
Requires:       crate(document-features-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/document-features)

%description -n %{name}+document-features
This metapackage enables feature "document-features" for the Rust ratatui crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+layout-cache
Summary:        Library that's all about cooking up terminal user interfaces - feature "layout-cache"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/std)
Requires:       crate(ratatui-core-0.1/layout-cache) >= 0.1.0
Provides:       crate(%{pkgname}/layout-cache)

%description -n %{name}+layout-cache
This metapackage enables feature "layout-cache" for the Rust ratatui crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+macros
Summary:        Library that's all about cooking up terminal user interfaces - feature "macros"
Requires:       crate(%{pkgname})
Requires:       crate(ratatui-macros-0.7/default) >= 0.7.0
Provides:       crate(%{pkgname}/macros)

%description -n %{name}+macros
This metapackage enables feature "macros" for the Rust ratatui crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+palette
Summary:        Library that's all about cooking up terminal user interfaces - feature "palette"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/std)
Requires:       crate(palette-0.7/default) >= 0.7.0
Requires:       crate(ratatui-core-0.1/palette) >= 0.1.0
Provides:       crate(%{pkgname}/palette)

%description -n %{name}+palette
This metapackage enables feature "palette" for the Rust ratatui crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+portable-atomic
Summary:        Library that's all about cooking up terminal user interfaces - feature "portable-atomic"
Requires:       crate(%{pkgname})
Requires:       crate(ratatui-core-0.1/portable-atomic) >= 0.1.0
Provides:       crate(%{pkgname}/portable-atomic)

%description -n %{name}+portable-atomic
This metapackage enables feature "portable-atomic" for the Rust ratatui crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+scrolling-regions
Summary:        Library that's all about cooking up terminal user interfaces - feature "scrolling-regions"
Requires:       crate(%{pkgname})
Requires:       crate(ratatui-core-0.1/scrolling-regions) >= 0.1.0
Requires:       crate(ratatui-crossterm-0.1/scrolling-regions) >= 0.1.0
Requires:       crate(ratatui-termion-0.1/scrolling-regions) >= 0.1.0
Requires:       crate(ratatui-termwiz-0.1/scrolling-regions) >= 0.1.0
Provides:       crate(%{pkgname}/scrolling-regions)

%description -n %{name}+scrolling-regions
This metapackage enables feature "scrolling-regions" for the Rust ratatui crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Library that's all about cooking up terminal user interfaces - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/std)
Requires:       crate(ratatui-core-0.1/serde) >= 0.1.0
Requires:       crate(ratatui-crossterm-0.1/serde) >= 0.1.0
Requires:       crate(ratatui-termion-0.1/serde) >= 0.1.0
Requires:       crate(ratatui-termwiz-0.1/serde) >= 0.1.0
Requires:       crate(ratatui-widgets-0.3/serde) >= 0.3.0
Requires:       crate(serde-1.0/default) >= 1.0.228
Requires:       crate(serde-1.0/derive) >= 1.0.228
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust ratatui crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Library that's all about cooking up terminal user interfaces - feature "std"
Requires:       crate(%{pkgname})
Requires:       crate(ratatui-core-0.1/std) >= 0.1.0
Requires:       crate(ratatui-widgets-0.3/std) >= 0.3.0
Provides:       crate(%{pkgname}/std)

%description -n %{name}+std
This metapackage enables feature "std" for the Rust ratatui crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+termion
Summary:        Library that's all about cooking up terminal user interfaces - feature "termion"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/std)
Requires:       crate(ratatui-termion-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/termion)

%description -n %{name}+termion
This metapackage enables feature "termion" for the Rust ratatui crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+termwiz
Summary:        Library that's all about cooking up terminal user interfaces - feature "termwiz"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/std)
Requires:       crate(ratatui-termwiz-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/termwiz)

%description -n %{name}+termwiz
This metapackage enables feature "termwiz" for the Rust ratatui crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+underline-color
Summary:        Library that's all about cooking up terminal user interfaces - feature "underline-color"
Requires:       crate(%{pkgname})
Requires:       crate(ratatui-core-0.1/underline-color) >= 0.1.0
Requires:       crate(ratatui-crossterm-0.1/underline-color) >= 0.1.0
Requires:       crate(ratatui-termwiz-0.1/underline-color) >= 0.1.0
Provides:       crate(%{pkgname}/underline-color)

%description -n %{name}+underline-color
This metapackage enables feature "underline-color" for the Rust ratatui crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable
Summary:        Library that's all about cooking up terminal user interfaces - feature "unstable"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/unstable-backend-writer)
Requires:       crate(%{pkgname}/unstable-rendered-line-info)
Requires:       crate(%{pkgname}/unstable-widget-ref)
Provides:       crate(%{pkgname}/unstable)

%description -n %{name}+unstable
This metapackage enables feature "unstable" for the Rust ratatui crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable-backend-writer
Summary:        Library that's all about cooking up terminal user interfaces - feature "unstable-backend-writer"
Requires:       crate(%{pkgname})
Requires:       crate(ratatui-crossterm-0.1/unstable-backend-writer) >= 0.1.0
Requires:       crate(ratatui-termion-0.1/unstable-backend-writer) >= 0.1.0
Provides:       crate(%{pkgname}/unstable-backend-writer)

%description -n %{name}+unstable-backend-writer
This metapackage enables feature "unstable-backend-writer" for the Rust ratatui crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unstable-rendered-line-info
Summary:        Library that's all about cooking up terminal user interfaces - feature "unstable-rendered-line-info"
Requires:       crate(%{pkgname})
Requires:       crate(ratatui-widgets-0.3/unstable-rendered-line-info) >= 0.3.0
Provides:       crate(%{pkgname}/unstable-rendered-line-info)

%description -n %{name}+unstable-rendered-line-info
This metapackage enables feature "unstable-rendered-line-info" for the Rust ratatui crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+widget-calendar
Summary:        Library that's all about cooking up terminal user interfaces - feature "widget-calendar" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(ratatui-widgets-0.3/calendar) >= 0.3.0
Provides:       crate(%{pkgname}/all-widgets)
Provides:       crate(%{pkgname}/widget-calendar)

%description -n %{name}+widget-calendar
This metapackage enables feature "widget-calendar" for the Rust ratatui crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "all-widgets" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
