import {
  Children,
  Fragment,
  ReactElement,
  ReactNode,
  cloneElement,
  isValidElement,
  useMemo
} from "react";

type MapEntry = { phrase: string; href: string };

type SmartLinkerProps = {
  children: ReactNode;
  map: MapEntry[];
};

const SKIP_TAGS = new Set(["a", "code", "pre", "h1", "h2", "h3", "h4", "h5", "h6"]);

function linkText(text: string, used: Set<string>, map: MapEntry[]) {
  let nodes: ReactNode[] = [text];
  for (const { phrase, href } of map) {
    if (used.has(href)) continue;
    const regex = new RegExp(`(\\b${phrase.replace(/[.*+?^${}()|[\]\\]/g, "\\$&")}\\b)`, "i");
    const next: ReactNode[] = [];
    for (const node of nodes) {
      if (typeof node !== "string") {
        next.push(node);
        continue;
      }
      const parts = node.split(regex);
      if (parts.length === 1) {
        next.push(node);
        continue;
      }
      for (let i = 0; i < parts.length; i++) {
        const part = parts[i];
        if (regex.test(part)) {
          next.push(
            <a key={`${href}-${i}`} href={href}>
              {part}
            </a>
          );
          used.add(href);
        } else if (part) {
          next.push(part);
        }
      }
    }
    nodes = next;
  }
  return nodes;
}

function walk(node: ReactNode, used: Set<string>, map: MapEntry[]): ReactNode {
  if (typeof node === "string") return linkText(node, used, map);
  if (!isValidElement(node)) return node;
  const tag = typeof node.type === "string" ? node.type : undefined;
  if (tag && SKIP_TAGS.has(tag)) return node;
  const el = node as ReactElement<{ children?: ReactNode }>;
  const kids = el.props?.children;
  const newKids = Children.map(kids, (child) => walk(child as ReactNode, used, map));
  return cloneElement(el, {}, newKids);
}

const SmartLinker = ({ children, map }: SmartLinkerProps) => {
  const used = useMemo(() => new Set<string>(), []);
  return <Fragment>{walk(children, used, map)}</Fragment>;
};

export default SmartLinker;
