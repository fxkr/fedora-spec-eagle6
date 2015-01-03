Name:		eagle6
Version:	6.6.0
Release:	1%{?dist}
Summary:	CadSoft Eagle 6

Group:		Applications/Engineering
License:	proprietary
URL:		http://www.cadsoft.de/
Source0:	http://web.cadsoft.de/ftp/eagle/program/6.6/eagle-lin-6.6.0.run
Source1:	eagle6
Source2:	eagle6.desktop

BuildRequires: desktop-file-utils
Requires:	glibc(x86-32) libXrender(x86-32) libXrandr(x86-32) libXcursor(x86-32) freetype(x86-32) fontconfig(x86-32) libXi(x86-32) openssl-libs(x86-32) openssl-libs(x86-32)

%filter_from_requires /libssl.so.1.0.0/d; /libcrypto.so.1.0.0/d
%filter_setup

%description

%prep

mkdir -p "$_builddir/opt"
sed -e '1,/^__DATA__$/d' "%{_sourcedir}/eagle-lin-%{version}.run" | \
    tar --no-same-owner -xjC "%{_builddir}"

%build

%install

mkdir "%{buildroot}/opt"
cp -a "%{_builddir}/eagle-%{version}" "%{buildroot}/opt/%{name}"
chmod -R a-s "%{buildroot}/opt/%{name}"

mkdir "%{buildroot}/opt/%{name}/lib"
ln -s /usr/lib/libcrypto.so.10 "%{buildroot}/opt/%{name}/lib/libcrypto.so.1.0.0"
ln -s /usr/lib/libssl.so.10 "%{buildroot}/opt/%{name}/lib/libssl.so.1.0.0"

install -Dm755 "%{_sourcedir}/%{name}" "%{buildroot}%{_bindir}/%{name}"
install -Dm644 "%{buildroot}/opt/%{name}/doc/eagle.1" "%{buildroot}%{_mandir}/man1/eagle.1"

desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE2}

%files
/opt/%{name}
%{_datadir}/applications/%{name}.desktop
%{_bindir}/%{name}
%{_mandir}/man1/eagle.1.gz

%doc

%changelog

