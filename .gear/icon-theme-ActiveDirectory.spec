Name:    icon-theme-ActiveDirectory
Version: 0
Release: alt1

Summary: Icons for programs of Active Directory
License: GPLv3+
Group:   Graphical desktop/Other
Url:     https://github.com/LenkaDEA/admc_icons

Source: %name-%version.tar

%description
Icons theme for ADMC and GPUI.

%prep
%setup

%build

%install
mkdir -p %buildroot%_iconsdir/Active-Directory/16x16
cp -R 16x16 %buildroot%_iconsdir/Active-Directory
mkdir -p %buildroot%_iconsdir/Active-Directory/22x22
cp -R 22x22 %buildroot%_iconsdir/Active-Directory
install index.theme %buildroot%_iconsdir/Active-Directory
export ICON_AD='Active-Directory'


%files
%_iconsdir/Active-Directory

%changelog
* Mon Oct 02 2023 Elena Dyatlenko <lenka@altlinux> 1.0-alt1
- Created a package with a theme for programs of Active Directory
