# Worksheets

One template per layer. Fill top down. Example rows use a simple room booking app.

## L1

Concept inventory (Jackson).

| Concept | Purpose (one) | State | Actions | Operational principle |
|---|---|---|---|---|
| Reservation | Hold a resource for a person for a time | resource, person, slot | reserve, cancel, extend | After you reserve a room for a slot, nobody else can reserve it for that slot until you cancel |

Checks: one purpose per concept; the operational principle is a short story with "after
... then ..."; it can be tested.

## L2

ORCA object map (Prater; Johnson and Henderson).

| Object | Attributes | Relationships | Calls to action | Glossary status |
|---|---|---|---|---|
| Room | name, size, equipment | has many Reservations | reserve, view schedule | Confirmed |

Checks: every object name is in the glossary; no widget or layout words ("dropdown",
"left panel").

## L3

Object-action matrix (Rosenberg). Cell values: `yes`, `no: <reason>`, `open`.

| Object \ Action | open | create | edit | delete | share | undo |
|---|---|---|---|---|---|---|
| Room | yes | no: admin only | no: admin only | no: admin only | yes | n/a |
| Reservation | yes | yes | yes | yes | yes | yes |

Checks: no cell without a value; every `no` has a reason; the same action means the same
thing in every row.

## L4

Posture decision (Cooper).

| Surface | Posture | Evidence (persona, frequency, duration) | Chrome budget |
|---|---|---|---|
| Booking app | transient | Staff book a room 2 to 3 times a week, under one minute | One primary action visible, no permanent side bars |

Postures: sovereign (open all day, main tool), transient (short visits, one task),
daemonic (runs in the background, rare contact).

## L5

Layer model (Material 1 environment; Liquid Glass).

| z | Layer | Elements | Moves with content? |
|---|---|---|---|
| 0 | Content | room list, schedule | yes |
| 1 | Functional | navigation, primary action | no |
| 2 | Transient | booking sheet, undo toast | no, dismissible |

## L6

Signifier and reversibility table (Norman; Shneiderman).

| Matrix cell | Signifier | Direct or command | Undo path |
|---|---|---|---|
| Reservation, delete | trash icon with label on the row | command | undo toast for 10 seconds, then in history |
| Reservation, edit time | drag handle on the slot | direct manipulation | drag back, or undo |

## L7

Motion rules (Apple, Designing Fluid Interfaces).

| Transition | Starts from | Interruptible | Redirectable |
|---|---|---|---|
| Booking sheet opens | tap on room | yes, swipe down at any time | yes, follows the finger |
