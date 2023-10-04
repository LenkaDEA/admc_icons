Name:    admc_icons
Version: 0
Release: alt1

Summary: Icons for ADMC
License: GPLv3+
Group:   Graphical desktop/Other
Url:     https://github.com/LenkaDEA/admc_icons

Source: %name-%version.tar

%description
Theme for ADMC.

%prep
%setup

%build

%install
mkdir -p %buildroot%_iconsdir/admc/64x64
cp -R 64x64 %buildroot%_iconsdir/admc
install index.theme %buildroot%_iconsdir/admc

%files
%_iconsdir/admc

%changelog
* Mon Oct 02 2023 Elena Dyatlenko <lenka@altlinux> 1.0-alt1
- Created a package with a theme for ADMC
