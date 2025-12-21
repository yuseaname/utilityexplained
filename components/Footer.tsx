import Link from "next/link";
import { legalLinks } from "@/lib/site";

const Footer = () => {
  return (
    <footer className="site-footer">
      <div className="container footer-inner">
        <div>
          <p className="footer-brand">Utility Plain English</p>
          <p className="footer-note">
            Informational content about home utilities and adulting. Not legal,
            financial, or professional advice.
          </p>
        </div>
        <div className="footer-links">
          {legalLinks.map((link) => (
            <Link key={link.href} href={link.href}>
              {link.name}
            </Link>
          ))}
        </div>
      </div>
    </footer>
  );
};

export default Footer;
