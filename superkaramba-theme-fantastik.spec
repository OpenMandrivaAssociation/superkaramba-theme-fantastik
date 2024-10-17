%define theme_name      fantastik

Summary:	Monitoring theme for superkaramba
Name:		superkaramba-theme-%{theme_name}
Version:	3.0
Release:	9
License:	GPL
Group:		Monitoring
Url:		https://kde-look.org/content/show.php?content=21396
Source0:	%{theme_name}-%{version}.tar.bz2
Requires:	superkaramba
BuildArch:	noarch

%description
This is a superkaramba theme which is a desktop applet 
that displays system information.

%files
%dir %{_datadir}/apps/superkaramba/themes/%{theme_name}
%{_datadir}/apps/superkaramba/themes/%{theme_name}/*

%post
if [ $1 = 1 ]; then
echo "THEME path=%{theme_name}/%{theme_name}.theme" >> %{_datadir}/apps/superkaramba/themes/default.theme
fi

%postun
if [ $1 = 0 ]; then
cat %{_datadir}/apps/superkaramba/themes/default.theme | grep -v "%{theme_name}" > %{_datadir}/apps/superkaramba/themes/default.theme
exit 0
fi

#----------------------------------------------------------------------------

%prep
%setup -q -n %{theme_name}-%{version}

%build

%install
mkdir -p %{buildroot}%{_datadir}/apps/superkaramba/themes/%{theme_name}
cp -rf * %{buildroot}%{_datadir}/apps/superkaramba/themes/%{theme_name}
chmod 755 %{buildroot}%{_datadir}/apps/superkaramba/themes/%{theme_name}/programs/mails_pop3.pl

