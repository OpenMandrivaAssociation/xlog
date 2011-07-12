Name:           xlog
Version:        2.0.5
Release:        %mkrel 1
Summary:        Logging program for Hamradio Operators
Group:          Communications
License:        GPLv3+
URL:            http://www.nongnu.org/xlog/
Source0:        http://download.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gtk2-devel
BuildRequires: libgnomeprint2-2-devel
BuildRequires: hamlib-devel
BuildRequires: shared-mime-info
BuildRequires: gettext-devel
BuildRequires: desktop-file-utils
Requires: hamlib


%description
xlog is a logging program for amateur radio operators. The log is stored
into a text file. QSO's are presented in a list. Items in the list can be
added, deleted or updated. For each contact, dxcc information is displayed
and bearings and distance is calculated, both short and long path.
xlog supports trlog, adif, cabrillo, edit, twlog and editest files.

%prep
%setup -q
#fix bogus .desktop file
sed -i -e "s/Utility;Database;HamRadio;GTK/Network;HamRadio;GTK/g" data/desktop/xlog.desktop
sed -i -e "s/.png//g" data/desktop/xlog.desktop

%build
%configure --enable-hamlib
%make

%install
rm -rf %{buildroot}
%makeinstall
rm -f %{buildroot}%{_datadir}/applications/mimeinfo.cache

%find_lang %{name}

desktop-file-install \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/xlog.desktop

%post
update-mime-database %{_datadir}/mime &> /dev/null || :

%postun
update-mime-database %{_datadir}/mime &> /dev/null || :

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS data/doc/BUGS ChangeLog NEWS README data/doc/TODO data/doc/manual data/doc/manual.tex data/glabels/qsllabels.glabels
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/dxcc
%{_datadir}/%{name}/maps
%{_datadir}/pixmaps/*
%{_datadir}/icons/gnome-mime-text-x-%{name}.png
%{_datadir}/icons/%{name}-icon.png
%{_datadir}/applications/*.desktop
%{_datadir}/mime/packages/*
%{_mandir}/man?/*


