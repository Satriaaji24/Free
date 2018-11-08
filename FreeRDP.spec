#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : FreeRDP
Version  : 2.0.0.rc3
Release  : 18
URL      : https://github.com/FreeRDP/FreeRDP/archive/2.0.0-rc3.tar.gz
Source0  : https://github.com/FreeRDP/FreeRDP/archive/2.0.0-rc3.tar.gz
Summary  : Free implementation of the Remote Desktop Protocol (RDP)
Group    : Development/Tools
License  : Apache-2.0
Requires: FreeRDP-bin = %{version}-%{release}
Requires: FreeRDP-data = %{version}-%{release}
Requires: FreeRDP-lib = %{version}-%{release}
Requires: FreeRDP-license = %{version}-%{release}
Requires: FreeRDP-man = %{version}-%{release}
BuildRequires : alsa-lib-dev
BuildRequires : buildreq-cmake
BuildRequires : cups-dev
BuildRequires : git
BuildRequires : glib-dev
BuildRequires : glibc-dev
BuildRequires : gst-plugins-base
BuildRequires : gst-plugins-base-dev
BuildRequires : gstreamer-dev
BuildRequires : icu4c-dev
BuildRequires : libSM-dev
BuildRequires : libX11-dev
BuildRequires : libXcursor-dev
BuildRequires : libXdamage-dev
BuildRequires : libXext-dev
BuildRequires : libXi-dev
BuildRequires : libXinerama-dev
BuildRequires : libXv-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libpng-dev
BuildRequires : libxkbfile-dev
BuildRequires : libxml2-dev
BuildRequires : libxshmfence
BuildRequires : libxslt-dev
BuildRequires : openssl-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(dbus-glib-1)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(wayland-scanner)
BuildRequires : pkgconfig(xcursor)
BuildRequires : pkgconfig(xkbcommon)
BuildRequires : pkgconfig(xrandr)
BuildRequires : pkgconfig(xrender)
BuildRequires : systemd-dev
Patch1: 0001-No-rc4-v2.patch

%description
FreeRDP is a open and free implementation of the Remote Desktop Protocol (RDP).
This package provides nightly master builds of all components.

%package bin
Summary: bin components for the FreeRDP package.
Group: Binaries
Requires: FreeRDP-data = %{version}-%{release}
Requires: FreeRDP-license = %{version}-%{release}
Requires: FreeRDP-man = %{version}-%{release}

%description bin
bin components for the FreeRDP package.


%package data
Summary: data components for the FreeRDP package.
Group: Data

%description data
data components for the FreeRDP package.


%package dev
Summary: dev components for the FreeRDP package.
Group: Development
Requires: FreeRDP-lib = %{version}-%{release}
Requires: FreeRDP-bin = %{version}-%{release}
Requires: FreeRDP-data = %{version}-%{release}
Provides: FreeRDP-devel = %{version}-%{release}

%description dev
dev components for the FreeRDP package.


%package lib
Summary: lib components for the FreeRDP package.
Group: Libraries
Requires: FreeRDP-data = %{version}-%{release}
Requires: FreeRDP-license = %{version}-%{release}

%description lib
lib components for the FreeRDP package.


%package license
Summary: license components for the FreeRDP package.
Group: Default

%description license
license components for the FreeRDP package.


%package man
Summary: man components for the FreeRDP package.
Group: Default

%description man
man components for the FreeRDP package.


%prep
%setup -q -n FreeRDP-2.0.0-rc3
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541706935
mkdir -p clr-build
pushd clr-build
%cmake .. -DWITH_ALSA=ON -DWITH_CHANNELS=ON -DWITH_CLIENT=ON -DWITH_CUPS=ON -DWITH_FFMPEG=OFF -DWITH_GSTREAMER_0_10=OFF -DWITH_GSTREAMER_1_0=ON -DWITH_JPEG=ON -DWITH_MANPAGES=ON -DWITH_OPENSSL=ON -DWITH_PULSE=ON -DWITH_SERVER=ON -DWITH_SHADOW_X11=ON -DWITH_SSE2=ON -DWITH_WAYLAND=ON -DWITH_X11=ON -DWITH_X264=OFF -DWITH_XCURSOR=ON -DWITH_XEXT=ON -DWITH_XI=ON -DWITH_XINERAMA=ON -DWITH_XKBFILE=ON -DWITH_XRENDER=ON -DWITH_XTEST=OFF -DWITH_XV=ON -DWITH_ZLIB=ON
make  %{?_smp_mflags} :|| cmake --build .
popd

%install
export SOURCE_DATE_EPOCH=1541706935
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/FreeRDP
cp LICENSE %{buildroot}/usr/share/package-licenses/FreeRDP/LICENSE
cp libfreerdp/core/license.c %{buildroot}/usr/share/package-licenses/FreeRDP/libfreerdp_core_license.c
cp libfreerdp/core/license.h %{buildroot}/usr/share/package-licenses/FreeRDP/libfreerdp_core_license.h
cp winpr/libwinpr/sysinfo/cpufeatures/NOTICE %{buildroot}/usr/share/package-licenses/FreeRDP/winpr_libwinpr_sysinfo_cpufeatures_NOTICE
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/freerdp-shadow-cli
/usr/bin/winpr-hash
/usr/bin/winpr-makecert
/usr/bin/wlfreerdp
/usr/bin/xfreerdp

%files data
%defattr(-,root,root,-)
/usr/share/abi/libfreerdp-client2.so.2.0.0.abi
/usr/share/abi/libfreerdp-client2.so.2.abi
/usr/share/abi/libfreerdp-server2.so.2.0.0.abi
/usr/share/abi/libfreerdp-server2.so.2.abi
/usr/share/abi/libfreerdp-shadow-subsystem2.so.2.0.0.abi
/usr/share/abi/libfreerdp-shadow-subsystem2.so.2.abi
/usr/share/abi/libfreerdp-shadow2.so.2.0.0.abi
/usr/share/abi/libfreerdp-shadow2.so.2.abi
/usr/share/abi/libfreerdp2.so.2.0.0.abi
/usr/share/abi/libfreerdp2.so.2.abi
/usr/share/abi/libuwac0.so.0.0.1.abi
/usr/share/abi/libuwac0.so.0.abi
/usr/share/abi/libwinpr-tools2.so.2.0.0.abi
/usr/share/abi/libwinpr-tools2.so.2.abi
/usr/share/abi/libwinpr2.so.2.0.0.abi
/usr/share/abi/libwinpr2.so.2.abi

%files dev
%defattr(-,root,root,-)
/usr/include/freerdp2/freerdp/addin.h
/usr/include/freerdp2/freerdp/altsec.h
/usr/include/freerdp2/freerdp/api.h
/usr/include/freerdp2/freerdp/assistance.h
/usr/include/freerdp2/freerdp/autodetect.h
/usr/include/freerdp2/freerdp/build-config.h
/usr/include/freerdp2/freerdp/cache/bitmap.h
/usr/include/freerdp2/freerdp/cache/brush.h
/usr/include/freerdp2/freerdp/cache/cache.h
/usr/include/freerdp2/freerdp/cache/glyph.h
/usr/include/freerdp2/freerdp/cache/nine_grid.h
/usr/include/freerdp2/freerdp/cache/offscreen.h
/usr/include/freerdp2/freerdp/cache/palette.h
/usr/include/freerdp2/freerdp/cache/pointer.h
/usr/include/freerdp2/freerdp/channels/audin.h
/usr/include/freerdp2/freerdp/channels/channels.h
/usr/include/freerdp2/freerdp/channels/cliprdr.h
/usr/include/freerdp2/freerdp/channels/encomsp.h
/usr/include/freerdp2/freerdp/channels/geometry.h
/usr/include/freerdp2/freerdp/channels/log.h
/usr/include/freerdp2/freerdp/channels/rail.h
/usr/include/freerdp2/freerdp/channels/rdpdr.h
/usr/include/freerdp2/freerdp/channels/rdpei.h
/usr/include/freerdp2/freerdp/channels/rdpgfx.h
/usr/include/freerdp2/freerdp/channels/rdpsnd.h
/usr/include/freerdp2/freerdp/channels/remdesk.h
/usr/include/freerdp2/freerdp/channels/tsmf.h
/usr/include/freerdp2/freerdp/channels/video.h
/usr/include/freerdp2/freerdp/channels/wtsvc.h
/usr/include/freerdp2/freerdp/client.h
/usr/include/freerdp2/freerdp/client/audin.h
/usr/include/freerdp2/freerdp/client/channels.h
/usr/include/freerdp2/freerdp/client/cliprdr.h
/usr/include/freerdp2/freerdp/client/cmdline.h
/usr/include/freerdp2/freerdp/client/disp.h
/usr/include/freerdp2/freerdp/client/drdynvc.h
/usr/include/freerdp2/freerdp/client/encomsp.h
/usr/include/freerdp2/freerdp/client/file.h
/usr/include/freerdp2/freerdp/client/geometry.h
/usr/include/freerdp2/freerdp/client/rail.h
/usr/include/freerdp2/freerdp/client/rdpei.h
/usr/include/freerdp2/freerdp/client/rdpgfx.h
/usr/include/freerdp2/freerdp/client/rdpsnd.h
/usr/include/freerdp2/freerdp/client/remdesk.h
/usr/include/freerdp2/freerdp/client/sshagent.h
/usr/include/freerdp2/freerdp/client/tsmf.h
/usr/include/freerdp2/freerdp/client/video.h
/usr/include/freerdp2/freerdp/codec/audio.h
/usr/include/freerdp2/freerdp/codec/bitmap.h
/usr/include/freerdp2/freerdp/codec/bulk.h
/usr/include/freerdp2/freerdp/codec/clear.h
/usr/include/freerdp2/freerdp/codec/color.h
/usr/include/freerdp2/freerdp/codec/dsp.h
/usr/include/freerdp2/freerdp/codec/h264.h
/usr/include/freerdp2/freerdp/codec/interleaved.h
/usr/include/freerdp2/freerdp/codec/jpeg.h
/usr/include/freerdp2/freerdp/codec/mppc.h
/usr/include/freerdp2/freerdp/codec/ncrush.h
/usr/include/freerdp2/freerdp/codec/nsc.h
/usr/include/freerdp2/freerdp/codec/planar.h
/usr/include/freerdp2/freerdp/codec/progressive.h
/usr/include/freerdp2/freerdp/codec/region.h
/usr/include/freerdp2/freerdp/codec/rfx.h
/usr/include/freerdp2/freerdp/codec/xcrush.h
/usr/include/freerdp2/freerdp/codec/yuv.h
/usr/include/freerdp2/freerdp/codec/zgfx.h
/usr/include/freerdp2/freerdp/codecs.h
/usr/include/freerdp2/freerdp/constants.h
/usr/include/freerdp2/freerdp/crypto/ber.h
/usr/include/freerdp2/freerdp/crypto/certificate.h
/usr/include/freerdp2/freerdp/crypto/crypto.h
/usr/include/freerdp2/freerdp/crypto/der.h
/usr/include/freerdp2/freerdp/crypto/er.h
/usr/include/freerdp2/freerdp/crypto/per.h
/usr/include/freerdp2/freerdp/crypto/tls.h
/usr/include/freerdp2/freerdp/dvc.h
/usr/include/freerdp2/freerdp/error.h
/usr/include/freerdp2/freerdp/event.h
/usr/include/freerdp2/freerdp/extension.h
/usr/include/freerdp2/freerdp/freerdp.h
/usr/include/freerdp2/freerdp/gdi/bitmap.h
/usr/include/freerdp2/freerdp/gdi/dc.h
/usr/include/freerdp2/freerdp/gdi/gdi.h
/usr/include/freerdp2/freerdp/gdi/gfx.h
/usr/include/freerdp2/freerdp/gdi/pen.h
/usr/include/freerdp2/freerdp/gdi/region.h
/usr/include/freerdp2/freerdp/gdi/shape.h
/usr/include/freerdp2/freerdp/gdi/video.h
/usr/include/freerdp2/freerdp/graphics.h
/usr/include/freerdp2/freerdp/input.h
/usr/include/freerdp2/freerdp/listener.h
/usr/include/freerdp2/freerdp/locale/keyboard.h
/usr/include/freerdp2/freerdp/locale/locale.h
/usr/include/freerdp2/freerdp/log.h
/usr/include/freerdp2/freerdp/message.h
/usr/include/freerdp2/freerdp/metrics.h
/usr/include/freerdp2/freerdp/peer.h
/usr/include/freerdp2/freerdp/pointer.h
/usr/include/freerdp2/freerdp/primary.h
/usr/include/freerdp2/freerdp/primitives.h
/usr/include/freerdp2/freerdp/rail.h
/usr/include/freerdp2/freerdp/scancode.h
/usr/include/freerdp2/freerdp/secondary.h
/usr/include/freerdp2/freerdp/server/audin.h
/usr/include/freerdp2/freerdp/server/channels.h
/usr/include/freerdp2/freerdp/server/cliprdr.h
/usr/include/freerdp2/freerdp/server/drdynvc.h
/usr/include/freerdp2/freerdp/server/echo.h
/usr/include/freerdp2/freerdp/server/encomsp.h
/usr/include/freerdp2/freerdp/server/rdpdr.h
/usr/include/freerdp2/freerdp/server/rdpei.h
/usr/include/freerdp2/freerdp/server/rdpgfx.h
/usr/include/freerdp2/freerdp/server/rdpsnd.h
/usr/include/freerdp2/freerdp/server/remdesk.h
/usr/include/freerdp2/freerdp/server/shadow.h
/usr/include/freerdp2/freerdp/session.h
/usr/include/freerdp2/freerdp/settings.h
/usr/include/freerdp2/freerdp/svc.h
/usr/include/freerdp2/freerdp/types.h
/usr/include/freerdp2/freerdp/update.h
/usr/include/freerdp2/freerdp/utils/msusb.h
/usr/include/freerdp2/freerdp/utils/passphrase.h
/usr/include/freerdp2/freerdp/utils/pcap.h
/usr/include/freerdp2/freerdp/utils/profiler.h
/usr/include/freerdp2/freerdp/utils/ringbuffer.h
/usr/include/freerdp2/freerdp/utils/signal.h
/usr/include/freerdp2/freerdp/utils/stopwatch.h
/usr/include/freerdp2/freerdp/version.h
/usr/include/freerdp2/freerdp/window.h
/usr/include/uwac0/uwac/uwac-tools.h
/usr/include/uwac0/uwac/uwac.h
/usr/include/winpr2/winpr/asn1.h
/usr/include/winpr2/winpr/bcrypt.h
/usr/include/winpr2/winpr/bitstream.h
/usr/include/winpr2/winpr/clipboard.h
/usr/include/winpr2/winpr/cmdline.h
/usr/include/winpr2/winpr/collections.h
/usr/include/winpr2/winpr/comm.h
/usr/include/winpr2/winpr/credentials.h
/usr/include/winpr2/winpr/credui.h
/usr/include/winpr2/winpr/crt.h
/usr/include/winpr2/winpr/crypto.h
/usr/include/winpr2/winpr/debug.h
/usr/include/winpr2/winpr/dsparse.h
/usr/include/winpr2/winpr/endian.h
/usr/include/winpr2/winpr/environment.h
/usr/include/winpr2/winpr/error.h
/usr/include/winpr2/winpr/file.h
/usr/include/winpr2/winpr/handle.h
/usr/include/winpr2/winpr/heap.h
/usr/include/winpr2/winpr/image.h
/usr/include/winpr2/winpr/ini.h
/usr/include/winpr2/winpr/input.h
/usr/include/winpr2/winpr/interlocked.h
/usr/include/winpr2/winpr/intrin.h
/usr/include/winpr2/winpr/io.h
/usr/include/winpr2/winpr/library.h
/usr/include/winpr2/winpr/locale.h
/usr/include/winpr2/winpr/memory.h
/usr/include/winpr2/winpr/midl.h
/usr/include/winpr2/winpr/ndr.h
/usr/include/winpr2/winpr/nt.h
/usr/include/winpr2/winpr/ntlm.h
/usr/include/winpr2/winpr/pack.h
/usr/include/winpr2/winpr/path.h
/usr/include/winpr2/winpr/pipe.h
/usr/include/winpr2/winpr/platform.h
/usr/include/winpr2/winpr/pool.h
/usr/include/winpr2/winpr/print.h
/usr/include/winpr2/winpr/registry.h
/usr/include/winpr2/winpr/rpc.h
/usr/include/winpr2/winpr/sam.h
/usr/include/winpr2/winpr/schannel.h
/usr/include/winpr2/winpr/security.h
/usr/include/winpr2/winpr/shell.h
/usr/include/winpr2/winpr/smartcard.h
/usr/include/winpr2/winpr/spec.h
/usr/include/winpr2/winpr/ssl.h
/usr/include/winpr2/winpr/sspi.h
/usr/include/winpr2/winpr/sspicli.h
/usr/include/winpr2/winpr/stream.h
/usr/include/winpr2/winpr/string.h
/usr/include/winpr2/winpr/strlst.h
/usr/include/winpr2/winpr/synch.h
/usr/include/winpr2/winpr/sysinfo.h
/usr/include/winpr2/winpr/tchar.h
/usr/include/winpr2/winpr/thread.h
/usr/include/winpr2/winpr/timezone.h
/usr/include/winpr2/winpr/tools/makecert.h
/usr/include/winpr2/winpr/user.h
/usr/include/winpr2/winpr/version.h
/usr/include/winpr2/winpr/windows.h
/usr/include/winpr2/winpr/winhttp.h
/usr/include/winpr2/winpr/winpr.h
/usr/include/winpr2/winpr/winsock.h
/usr/include/winpr2/winpr/wlog.h
/usr/include/winpr2/winpr/wnd.h
/usr/include/winpr2/winpr/wtsapi.h
/usr/include/winpr2/winpr/wtypes.h
/usr/lib64/cmake/FreeRDP-Client2/FreeRDP-ClientConfig.cmake
/usr/lib64/cmake/FreeRDP-Client2/FreeRDP-ClientConfigVersion.cmake
/usr/lib64/cmake/FreeRDP-Client2/FreeRDP-ClientTargets-relwithdebinfo.cmake
/usr/lib64/cmake/FreeRDP-Client2/FreeRDP-ClientTargets.cmake
/usr/lib64/cmake/FreeRDP-Server2/FreeRDP-ServerConfig.cmake
/usr/lib64/cmake/FreeRDP-Server2/FreeRDP-ServerConfigVersion.cmake
/usr/lib64/cmake/FreeRDP-Server2/FreeRDP-ServerTargets-relwithdebinfo.cmake
/usr/lib64/cmake/FreeRDP-Server2/FreeRDP-ServerTargets.cmake
/usr/lib64/cmake/FreeRDP-Shadow2/FreeRDP-ShadowConfig.cmake
/usr/lib64/cmake/FreeRDP-Shadow2/FreeRDP-ShadowConfigVersion.cmake
/usr/lib64/cmake/FreeRDP-Shadow2/FreeRDP-ShadowTargets-relwithdebinfo.cmake
/usr/lib64/cmake/FreeRDP-Shadow2/FreeRDP-ShadowTargets.cmake
/usr/lib64/cmake/FreeRDP2/FreeRDPConfig.cmake
/usr/lib64/cmake/FreeRDP2/FreeRDPConfigVersion.cmake
/usr/lib64/cmake/FreeRDP2/FreeRDPTargets-relwithdebinfo.cmake
/usr/lib64/cmake/FreeRDP2/FreeRDPTargets.cmake
/usr/lib64/cmake/WinPR2/WinPRConfig.cmake
/usr/lib64/cmake/WinPR2/WinPRConfigVersion.cmake
/usr/lib64/cmake/WinPR2/WinPRTargets-relwithdebinfo.cmake
/usr/lib64/cmake/WinPR2/WinPRTargets.cmake
/usr/lib64/cmake/uwac0/uwac-relwithdebinfo.cmake
/usr/lib64/cmake/uwac0/uwac.cmake
/usr/lib64/cmake/uwac0/uwacConfig.cmake
/usr/lib64/cmake/uwac0/uwacConfigVersion.cmake
/usr/lib64/libfreerdp-client2.so
/usr/lib64/libfreerdp-server2.so
/usr/lib64/libfreerdp-shadow-subsystem2.so
/usr/lib64/libfreerdp-shadow2.so
/usr/lib64/libfreerdp2.so
/usr/lib64/libuwac0.so
/usr/lib64/libwinpr-tools2.so
/usr/lib64/libwinpr2.so
/usr/lib64/pkgconfig/freerdp-client2.pc
/usr/lib64/pkgconfig/freerdp-server2.pc
/usr/lib64/pkgconfig/freerdp-shadow2.pc
/usr/lib64/pkgconfig/freerdp2.pc
/usr/lib64/pkgconfig/uwac0.pc
/usr/lib64/pkgconfig/winpr-tools2.pc
/usr/lib64/pkgconfig/winpr2.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libfreerdp-client2.so.2
/usr/lib64/libfreerdp-client2.so.2.0.0
/usr/lib64/libfreerdp-server2.so.2
/usr/lib64/libfreerdp-server2.so.2.0.0
/usr/lib64/libfreerdp-shadow-subsystem2.so.2
/usr/lib64/libfreerdp-shadow-subsystem2.so.2.0.0
/usr/lib64/libfreerdp-shadow2.so.2
/usr/lib64/libfreerdp-shadow2.so.2.0.0
/usr/lib64/libfreerdp2.so.2
/usr/lib64/libfreerdp2.so.2.0.0
/usr/lib64/libuwac0.so.0
/usr/lib64/libuwac0.so.0.0.1
/usr/lib64/libwinpr-tools2.so.2
/usr/lib64/libwinpr-tools2.so.2.0.0
/usr/lib64/libwinpr2.so.2
/usr/lib64/libwinpr2.so.2.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/FreeRDP/LICENSE
/usr/share/package-licenses/FreeRDP/libfreerdp_core_license.c
/usr/share/package-licenses/FreeRDP/libfreerdp_core_license.h
/usr/share/package-licenses/FreeRDP/winpr_libwinpr_sysinfo_cpufeatures_NOTICE

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/freerdp-shadow-cli.1
/usr/share/man/man1/winpr-hash.1
/usr/share/man/man1/winpr-makecert.1
/usr/share/man/man1/wlfreerdp.1
/usr/share/man/man7/wlog.7
