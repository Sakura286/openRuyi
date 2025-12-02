# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           openRuyi-repos
Version:        2
Release:        %autorelease
Summary:        openRuyi repository files
License:        MulanPSL-2.0
URL:            https://www.openruyi.org
Source0:        openRuyi-riscv64.repo
Source1:        openRuyi-amd64.repo

Provides:       system-repos

%description
This package contains the repository files for openRuyi.

%prep

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}/yum.repos.d/
%ifarch riscv64
install -c -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/openRuyi.repo
%endif
%ifarch x86_64
install -c -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/yum.repos.d/openRuyi.repo
%endif

%files
%defattr(644,root,root,755)
%config(noreplace) %{_sysconfdir}/yum.repos.d/openRuyi.repo

%changelog
%{?autochangelog}
