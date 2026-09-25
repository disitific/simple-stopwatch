pkgname=simple-stopwatch
pkgver=1.0
pkgrel=1
pkgdesc="A minimalist PyQt6 Timer application"
arch=('any')
license=('GPL')
depends=('python' 'python-pyqt6')
source=('main.py' 'simple-stopwatch.desktop')
sha256sums=('SKIP' 'SKIP')

package() {
    # 1. Install the Python script into /usr/bin/ and make it executable
    install -Dm755 "$srcdir/main.py" "$pkgdir/usr/bin/simple-stopwatch"

    # 2. Install the desktop entry file so the launcher sees it
    install -Dm644 "$srcdir/simple-stopwatch.desktop" "$pkgdir/usr/share/applications/simple-stopwatch.desktop"
}
