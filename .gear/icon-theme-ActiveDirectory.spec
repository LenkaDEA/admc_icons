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
mkdir -p %buildroot%_iconsdir/Active-Directory-line
cp -R Active-Directory-line %buildroot%_iconsdir

mkdir -p %buildroot%_iconsdir/Active-Directory-duotone
cp -R Active-Directory-duotone %buildroot%_iconsdir

mkdir -p %buildroot%_iconsdir/Active-Directory-color
cp -R Active-Directory-color %buildroot%_iconsdir

#mkdir -p %buildroot%_datadir/alt-management-console
install -m644 -D icon-theme.conf %buildroot%_datadir/alt-management-console/icon-theme.conf

%files
%_iconsdir/Active-Directory-line
%_iconsdir/Active-Directory-duotone
%_iconsdir/Active-Directory-color
%_datadir/alt-management-console/icon-theme.conf

%changelog
* Mon Oct 02 2023 Elena Dyatlenko <lenka@altlinux> 1.0-alt1
- Created a package with a theme for programs of Active Directory
