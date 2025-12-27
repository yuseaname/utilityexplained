import Link from "next/link";
import { navigation } from "@/lib/site";
import ThemeToggle from "@/components/ThemeToggle";

const Header = () => {
  return (
    <header className="site-header">
      <div className="container header-inner">
        <Link className="logo" href="/">
          Utility Explained
        </Link>
        <nav className="nav" aria-label="Primary">
          {navigation.map((item) => (
            <Link key={item.href} href={item.href} className="nav-link">
              {item.name}
            </Link>
          ))}
        </nav>
        <ThemeToggle />
      </div>
    </header>
  );
};

export default Header;
