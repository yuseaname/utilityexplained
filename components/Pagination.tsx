import Link from "next/link";

type PaginationProps = {
  basePath: string; // e.g. "/blog/page"
  current: number;
  totalPages: number;
};

const Pagination = ({ basePath, current, totalPages }: PaginationProps) => {
  if (totalPages <= 1) return null;
  const prev = current > 1 ? current - 1 : null;
  const next = current < totalPages ? current + 1 : null;
  return (
    <nav className="pagination" aria-label="Pagination" style={{ marginTop: 24 }}>
      <div style={{ display: "flex", gap: 12, alignItems: "center" }}>
        {prev ? <Link href={prev === 1 ? "/blog" : `${basePath}/${prev}`}>Prev</Link> : <span />}
        <span style={{ color: "var(--muted)" }}>
          Page {current} of {totalPages}
        </span>
        {next ? <Link href={`${basePath}/${next}`}>Next</Link> : <span />}
      </div>
    </nav>
  );
};

export default Pagination;
