import type { Post } from "@/lib/types";

export const utilityBillsProrationPastDueMinimumPosts_2025_12_26: Post[] = [
  {
    slug: "utility-bill-proration-explained",
    title: "Utility Bill Proration Explained: Why Your First or Final Bill Looks Weird",
    description:
      "If your first or final utility bill looks off, proration is usually the reason. This guide explains what it means, how to spot it, and how to sanity-check the math.",
    category: "Budgeting",
    keyword: "utility bill proration",
    date: "2025-12-26",
    readTime: "15 min read",
    image: {
      src: "/images/utility-bill.jpg",
      alt: "Person reviewing a utility statement with a calendar nearby"
    },
    relatedSlugs: [
      "utility-bills-costs-explained",
      "why-my-utility-bill-is-higher-with-same-usage",
      "estimated-utility-bill-explained",
      "past-due-balance-utility-bill-explained",
      "minimum-bill-utility-bill-explained"
    ],
    sections: [
      {
        id: "problem",
        title: "The problem: your bill does not match the month you lived there",
        content: (
          <>
            <p className="lead">
              You move in or move out, and the next utility bill looks strange. The
              dates do not line up with the calendar, the total feels too high or too
              low, and it is hard to tell what you are paying for.
            </p>
            <p>
              Most of the time, the answer is simple: the bill was{" "}
              <strong>prorated</strong>. That means the bill only covers part of a
              normal billing cycle, not a full month.
            </p>
            <p>
              This guide will make proration feel predictable. For the full billing
              model (usage, delivery, fixed fees), start here:
              <a href="/utility-bills-costs-explained"> Utility Bills &amp; Costs Explained</a>.
            </p>
          </>
        )
      },
      {
        id: "toc",
        title: "Table of contents",
        content: (
          <>
            <ul>
              <li><a href="#quick-answer">The quick answer</a></li>
              <li><a href="#why-happens">Why proration happens</a></li>
              <li><a href="#spot-proration">How to spot proration on your bill</a></li>
              <li><a href="#sanity-check">A simple sanity-check method</a></li>
              <li><a href="#misconceptions">Common misconceptions</a></li>
              <li><a href="#faqs">FAQs</a></li>
            </ul>
          </>
        )
      },
      {
        id: "quick-answer",
        title: "The quick answer",
        content: (
          <>
            <p>
              <strong>Proration</strong> means your utility bill covers only part of
              a billing cycle. It is common when service starts or ends in the middle
              of a cycle, like a move-in or move-out.
            </p>
            <p>
              The bill is not wrong just because the dates look unusual. It is a
              partial-period bill, and the math should be based on the actual days of
              service.
            </p>
          </>
        )
      },
      {
        id: "why-happens",
        title: "Why proration happens (plain English)",
        content: (
          <>
            <p>
              Utilities do not bill by calendar months. They bill by fixed billing
              cycles, and your start or end date rarely matches those cycles.
            </p>
            <h3>Billing cycles do not align with your move-in or move-out</h3>
            <p>
              If the billing cycle runs from the 5th to the 4th, and you moved in on
              the 18th, your first bill will only include the 18th to the 4th. That
              is a partial cycle.
            </p>
            <h3>Meter read dates and bill dates are different</h3>
            <p>
              Your bill may show a meter read date, a service period, and a bill
              issue date. Those are not the same thing. The service period is the
              key date range for proration.
            </p>
            <p>
              If you are also seeing an estimated read, the timing can look even
              more confusing. This helps:
              <a href="/blog/estimated-utility-bill-explained"> estimated utility bill explained</a>.
            </p>
          </>
        )
      },
      {
        id: "spot-proration",
        title: "How to spot proration on your bill",
        content: (
          <>
            <p>
              Look for the service period dates and compare them to your move-in or
              move-out date.
            </p>
            <h3>Where the dates appear</h3>
            <p>
              Most bills list a service period near the top, often labeled “Service
              Dates,” “Billing Period,” or “Usage Period.”
            </p>
            <h3>Terms you might see</h3>
            <ul>
              <li>Prorated or pro-rated</li>
              <li>Partial month</li>
              <li>Service start date / service end date</li>
            </ul>
          </>
        )
      },
      {
        id: "sanity-check",
        title: "A simple sanity-check method (no advanced math)",
        content: (
          <>
            <p>
              You do not need a calculator spreadsheet. Use a few simple checks.
            </p>
            <h3>1) Count the billing days</h3>
            <p>
              Count the number of days in the service period. A 17-day bill should
              not be compared to a 30-day bill without adjusting.
            </p>
            <h3>2) Normalize usage per day</h3>
            <p>
              Divide usage by billing days. This makes a partial month comparable to
              a normal month. If the total still looks off, this guide explains why:
              <a href="/blog/why-my-utility-bill-is-higher-with-same-usage"> why a bill can be higher with the same usage</a>.
            </p>
            <h3>3) Separate usage from fixed charges</h3>
            <p>
              A partial month can still include fixed charges. That is why low usage
              does not always mean a tiny total. If this surprises you, read:
              <a href="/blog/minimum-bill-utility-bill-explained"> minimum bill explained</a>.
            </p>
            <p>
              If your final bill also shows a past-due line, this article clarifies
              what that means:
              <a href="/blog/past-due-balance-utility-bill-explained"> past due balance explained</a>.
            </p>
          </>
        )
      },
      {
        id: "misconceptions",
        title: "Common misconceptions",
        content: (
          <>
            <ul>
              <li>
                <strong>“Prorated means the utility guessed.”</strong> Not necessarily.
                It just means the bill covers part of the cycle.
              </li>
              <li>
                <strong>“A short period should be almost free.”</strong> Fixed charges
                can still apply even for partial months.
              </li>
              <li>
                <strong>“The bill date is the same as the usage period.”</strong> The
                usage period is what matters for proration.
              </li>
            </ul>
          </>
        )
      }
    ],
    faqs: [
      {
        question: "What does prorated mean on a utility bill?",
        answer:
          "It means the bill covers only part of a normal billing cycle, usually because service started or ended mid-cycle."
      },
      {
        question: "Why is my first utility bill so high or low?",
        answer:
          "First bills are often prorated and may include fixed charges or deposits. Check the service period dates and billing days first."
      },
      {
        question: "How do I check a prorated utility bill?",
        answer:
          "Count the billing days in the service period, then compare usage per day instead of total usage. This shows whether the rate looks consistent."
      },
      {
        question: "Is proration the same as an estimated bill?",
        answer:
          "No. Proration is about partial billing periods. Estimated bills are about how usage was measured. A bill can be prorated, estimated, or both."
      },
      {
        question: "Does proration affect fixed charges?",
        answer:
          "Many fixed charges still apply even for partial months, which is why a short period can still have a noticeable total."
      }
    ]
  },
  {
    slug: "past-due-balance-utility-bill-explained",
    title: "Past Due Balance and Late Fees on a Utility Bill Explained (and What a Disconnect Notice Really Means)",
    description:
      "Seeing a past due balance or late fee? This guide explains how bill dates, due dates, and payment posting work, and what a disconnect notice really signals.",
    category: "Budgeting",
    keyword: "past due balance on utility bill",
    date: "2025-12-26",
    readTime: "16 min read",
    image: {
      src: "/images/utility-bill.jpg",
      alt: "Utility bills with a due date highlighted on a calendar"
    },
    relatedSlugs: [
      "utility-bills-costs-explained",
      "budget-billing-level-pay-explained",
      "estimated-utility-bill-explained",
      "why-my-utility-bill-is-higher-with-same-usage",
      "utility-bill-proration-explained",
      "minimum-bill-utility-bill-explained"
    ],
    sections: [
      {
        id: "problem",
        title: "The problem: a past-due line shows up when you thought you paid",
        content: (
          <>
            <p className="lead">
              You open your bill and see “past due,” a late fee, or even a
              disconnect notice. It feels urgent, and it is not always clear why it
              happened.
            </p>
            <p>
              The most common cause is timing: bill date, due date, and payment
              posting date are three different things. Once you know the timing,
              the line usually makes sense.
            </p>
            <p>
              For the full billing structure (usage vs delivery vs fixed charges),
              start here:
              <a href="/utility-bills-costs-explained"> Utility Bills &amp; Costs Explained</a>.
            </p>
          </>
        )
      },
      {
        id: "toc",
        title: "Table of contents",
        content: (
          <>
            <ul>
              <li><a href="#quick-answer">The quick answer</a></li>
              <li><a href="#dates">Bill date vs due date vs posting date</a></li>
              <li><a href="#late-fees">How late fees are typically calculated</a></li>
              <li><a href="#disconnect">What a disconnect notice really means</a></li>
              <li><a href="#what-to-do">What to do right now (simple steps)</a></li>
              <li><a href="#misconceptions">Common misconceptions</a></li>
              <li><a href="#faqs">FAQs</a></li>
            </ul>
          </>
        )
      },
      {
        id: "quick-answer",
        title: "The quick answer",
        content: (
          <>
            <p>
              A <strong>past due balance</strong> means the utility did not receive
              or post payment by the stated due date. A late fee is a penalty tied
              to that timing, not necessarily to your usage.
            </p>
            <p>
              A disconnect notice is usually a warning step in a sequence. It does
              not always mean service will stop immediately, but it does mean the
              utility wants attention.
            </p>
          </>
        )
      },
      {
        id: "dates",
        title: "Bill date vs due date vs payment posting date",
        content: (
          <>
            <p>
              Three dates create most of the confusion:
            </p>
            <ul>
              <li>
                <strong>Bill date:</strong> when the bill is generated.
              </li>
              <li>
                <strong>Due date:</strong> the deadline to avoid a past-due status.
              </li>
              <li>
                <strong>Posting date:</strong> when the payment is recorded by the utility.
              </li>
            </ul>
            <p>
              If you paid close to the due date, weekends, holidays, or payment
              processing can push the posting date later, which can trigger a past-due
              line even if you paid on time.
            </p>
          </>
        )
      },
      {
        id: "late-fees",
        title: "How late fees are typically calculated (simple examples)",
        content: (
          <>
            <p>
              Late fees vary by utility, but they usually follow one of two models:
            </p>
            <ul>
              <li><strong>Flat fee:</strong> a set dollar amount if the bill is late.</li>
              <li><strong>Percentage fee:</strong> a small percent of the past-due amount.</li>
            </ul>
            <p>
              This is why the total can change even when your usage does not. If your
              bill looks higher with similar usage, this checklist helps:
              <a href="/blog/why-my-utility-bill-is-higher-with-same-usage"> bill higher with same usage</a>.
            </p>
          </>
        )
      },
      {
        id: "disconnect",
        title: "What a disconnect notice really means",
        content: (
          <>
            <p>
              A disconnect notice is typically a formal warning. It signals that the
              account is delinquent and action is needed, but it is usually part of a
              timeline that includes notices and deadlines.
            </p>
            <p>
              If your bill was also estimated or corrected, that can create surprise
              balances. This explains the estimate piece:
              <a href="/blog/estimated-utility-bill-explained"> estimated utility bill explained</a>.
            </p>
          </>
        )
      },
      {
        id: "what-to-do",
        title: "What to do right now (simple steps, no drama)",
        content: (
          <>
            <p>
              You do not need a long plan. Start with these simple checks:
            </p>
            <ol>
              <li>
                <strong>Confirm payment status</strong> in your bank or payment method.
              </li>
              <li>
                <strong>Check the posting date</strong> on the utility account if it is listed.
              </li>
              <li>
                <strong>Review the bill dates</strong> to see if timing explains the past-due line.
              </li>
            </ol>
            <p>
              If you want more predictable monthly totals, budget billing can help
              smooth payment timing:
              <a href="/blog/budget-billing-level-pay-explained"> budget billing explained</a>.
            </p>
            <p>
              If a move created timing confusion, this companion guide can help:
              <a href="/blog/utility-bill-proration-explained"> proration explained</a>.
            </p>
          </>
        )
      },
      {
        id: "misconceptions",
        title: "Common misconceptions",
        content: (
          <>
            <ul>
              <li>
                <strong>“Past due means I did not pay.”</strong> It can also mean the
                payment posted after the due date.
              </li>
              <li>
                <strong>“A disconnect notice means service ends today.”</strong> It is
                usually a warning step, not immediate shutoff.
              </li>
              <li>
                <strong>“Late fees are tied to usage.”</strong> Late fees are tied to
                payment timing.
              </li>
            </ul>
          </>
        )
      }
    ],
    faqs: [
      {
        question: "What does past due mean on a utility bill?",
        answer:
          "It means the payment was not received or posted by the due date, so the balance carried forward."
      },
      {
        question: "Why did I get a late fee if I paid on time?",
        answer:
          "Payments made close to the due date can post after the deadline due to processing time, weekends, or holidays."
      },
      {
        question: "What does a disconnect notice mean?",
        answer:
          "It is a formal warning that the account is delinquent and action is needed. It usually comes with a timeline and is not always immediate shutoff."
      },
      {
        question: "Can a bill look past due because of an estimated read?",
        answer:
          "An estimated read can lead to a correction later, which might add to the balance. The past-due status still relates to payment timing."
      },
      {
        question: "How can I avoid late fees going forward?",
        answer:
          "Know the due date and give payments enough time to post. If available, consider automatic payments or reminders to avoid timing issues."
      }
    ]
  },
  {
    slug: "minimum-bill-utility-bill-explained",
    title: "Minimum Bill or Minimum Charge on a Utility Bill Explained (Why the Total Is Not Zero)",
    description:
      "Used very little but still got a bill? This guide explains minimum charges, how they differ from customer charges, and how to find them on your statement.",
    category: "Budgeting",
    keyword: "minimum bill on utility bill",
    date: "2025-12-26",
    readTime: "14 min read",
    image: {
      src: "/images/utility-bill.jpg",
      alt: "Utility statement with a small total highlighted"
    },
    relatedSlugs: [
      "utility-bills-costs-explained",
      "why-my-utility-bill-is-higher-with-same-usage",
      "estimated-utility-bill-explained",
      "electric-bill-breakdown-understanding-line-items",
      "utility-bill-proration-explained",
      "past-due-balance-utility-bill-explained"
    ],
    sections: [
      {
        id: "problem",
        title: "The problem: you used almost nothing, but the bill is not zero",
        content: (
          <>
            <p className="lead">
              You used very little, maybe almost nothing, and the bill still shows a
              charge. It can feel like you are paying for air.
            </p>
            <p>
              In many utility systems, that line is a <strong>minimum bill</strong>
              or <strong>minimum charge</strong>. It is a common part of the rate
              structure, not a mistake.
            </p>
            <p>
              For the full billing framework, start here:
              <a href="/utility-bills-costs-explained"> Utility Bills &amp; Costs Explained</a>.
            </p>
          </>
        )
      },
      {
        id: "toc",
        title: "Table of contents",
        content: (
          <>
            <ul>
              <li><a href="#quick-answer">The quick answer</a></li>
              <li><a href="#why-minimum">Why utilities use minimum bills</a></li>
              <li><a href="#difference">Minimum bill vs customer charge</a></li>
              <li><a href="#where-find">How to find it on your statement</a></li>
              <li><a href="#savings">How it affects savings expectations</a></li>
              <li><a href="#misconceptions">Common misconceptions</a></li>
              <li><a href="#faqs">FAQs</a></li>
            </ul>
          </>
        )
      },
      {
        id: "quick-answer",
        title: "The quick answer",
        content: (
          <>
            <p>
              A <strong>minimum bill</strong> is a set amount you pay even if your
              usage is very low. If your calculated charges fall below that minimum,
              the utility raises the total to the minimum amount.
            </p>
            <p>
              It is different from a usage charge. Think of it as a floor, not a
              per-unit rate.
            </p>
          </>
        )
      },
      {
        id: "why-minimum",
        title: "Why utilities use minimum bills",
        content: (
          <>
            <p>
              Utilities have baseline costs that do not disappear when usage is low.
              A minimum bill helps cover those costs so service can stay available.
            </p>
            <p>
              It is not meant to punish low usage. It is a way of keeping the system
              stable and the account active.
            </p>
          </>
        )
      },
      {
        id: "difference",
        title: "Minimum bill vs customer charge (simple rules)",
        content: (
          <>
            <p>
              These two are easy to confuse. Here is the simplest way to separate them.
            </p>
            <h3>When the minimum replaces other charges</h3>
            <p>
              In some rate designs, the minimum bill is a floor. If your normal
              charges fall below that floor, the minimum replaces them.
            </p>
            <h3>When the minimum stacks with other charges</h3>
            <p>
              In other cases, a customer charge is fixed and always appears, while
              the minimum applies only if the total is still below the minimum.
            </p>
            <p>
              If you want to see how line items are grouped, this breakdown helps:
              <a href="/blog/electric-bill-breakdown-understanding-line-items"> line items explained</a>.
            </p>
          </>
        )
      },
      {
        id: "where-find",
        title: "How to find a minimum bill on your statement",
        content: (
          <>
            <p>
              Look for terms like:
            </p>
            <ul>
              <li>Minimum bill</li>
              <li>Minimum charge</li>
              <li>Minimum monthly charge</li>
              <li>Service minimum</li>
            </ul>
            <p>
              It may appear in the usage section or near fixed charges, depending on
              the utility format.
            </p>
          </>
        )
      },
      {
        id: "savings",
        title: "How it affects savings expectations",
        content: (
          <>
            <p>
              A minimum bill changes the math of saving. If your total is already at
              the minimum, lowering usage further may not reduce the total.
            </p>
            <p>
              This is why two months with very low usage can still have the same
              total. If that feels confusing, this guide helps:
              <a href="/blog/why-my-utility-bill-is-higher-with-same-usage"> why a bill can be higher with the same usage</a>.
            </p>
            <p>
              If your bill was also prorated after a move, that can add another layer
              of confusion. See:
              <a href="/blog/utility-bill-proration-explained"> proration explained</a>.
            </p>
          </>
        )
      },
      {
        id: "misconceptions",
        title: "Common misconceptions",
        content: (
          <>
            <ul>
              <li>
                <strong>“Minimum means I must have used that much.”</strong> It is a
                billing floor, not a usage amount.
              </li>
              <li>
                <strong>“Minimum bill is the same as a late fee.”</strong> It is not.
                Late fees relate to payment timing.
              </li>
              <li>
                <strong>“If I use zero, my bill must be zero.”</strong> Some utilities
                still apply a minimum to keep service active.
              </li>
            </ul>
          </>
        )
      }
    ],
    faqs: [
      {
        question: "What is a minimum bill on a utility bill?",
        answer:
          "It is a set minimum amount you pay even if your usage-based charges are very low. If your calculated charges fall below that amount, the bill is raised to the minimum."
      },
      {
        question: "Is a minimum bill the same as a customer charge?",
        answer:
          "Not always. A customer charge is usually a fixed line item, while a minimum bill is a floor that may replace or supplement other charges depending on the rate design."
      },
      {
        question: "Why do I have a minimum bill when I used almost nothing?",
        answer:
          "Minimum bills help cover baseline service costs and keep the account active even in low-usage months."
      },
      {
        question: "Where can I find the minimum bill on my statement?",
        answer:
          "Look for labels like minimum bill, minimum charge, or minimum monthly charge. It may appear near fixed charges or the usage summary."
      },
      {
        question: "Can a minimum bill apply on a prorated month?",
        answer:
          "Yes. Some utilities still apply a minimum even for partial months, which can make a short period look higher than expected."
      }
    ]
  }
];
