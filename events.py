"""
events.py - The Random Municipal Event Engine.
Every event is real. No, we will not specify which ones.
"""

import random
from dataclasses import dataclass, field
from typing import List


@dataclass
class Option:
    label: str
    cost_text: str
    effects: dict
    result: str
    followup: str = ""


@dataclass
class Event:
    title: str
    description: str
    options: List[Option] = field(default_factory=list)


EVENT_LIBRARY: List[Event] = [
    Event(
        "MAJOR ROAD HAS COLLAPSED.",
        "A road opened yesterday has opened further today. It is now a hole with ambitions.",
        [
            Option("A. Repair immediately", "Rp 80 B", {"budget": -80, "infrastructure": 8, "satisfaction": 4}, "The road is repaired."),
            Option("B. Conduct a feasibility study", "Rp 10 B", {"budget": -10, "bureaucracy": 8, "feasibility_studies": 1, "traffic": 4, "project_progress": -2}, "A feasibility study is commissioned. The road will wait. The road is patient."),
            Option("C. Hold a coordination meeting", "Rp 2 B", {"budget": -2, "bureaucracy": 15, "meetings": 1, "satisfaction": -3}, "Eleven agencies agree that the hole exists.", "This is considered progress."),
            Option("D. Do absolutely nothing", "Rp 0 B", {"traffic": 12, "satisfaction": -10, "infrastructure": -5}, "The hole is now a landmark. Locals have named it."),
        ],
    ),
    Event(
        "HEAVY RAIN DETECTED.",
        "Meteorology confirms water is falling from the sky, as it has done for millions of years. Panic anyway.",
        [
            Option("A. Activate pumps", "Rp 20 B", {"budget": -20, "flood_risk": -10}, "Pumps activated. Three of eleven are functional. Flood risk reduced proportionally to optimism."),
            Option("B. Clean drainage", "Rp 30 B", {"budget": -30, "flood_risk": -15, "infrastructure": 2}, "Drainage cleaned. Items recovered: 4 mattresses, 1 motorcycle, 2019 budget report."),
            Option("C. Emergency meeting", "Rp 5 B", {"budget": -5, "bureaucracy": 12, "meetings": 1, "flood_risk": 3}, "A meeting is held while water rises past the meeting room window."),
            Option("D. Blame the weather", "Rp 0 B", {"satisfaction": -3}, "Nothing happens. The weather, unimpressed, continues."),
        ],
    ),
    Event(
        "TRAFFIC JAM OF HISTORIC PROPORTIONS.",
        "A jam has formed on the toll road. Satellites can see it. Cartographers are considering labeling it.",
        [
            Option("A. Deploy traffic officers", "Rp 15 B", {"budget": -15, "traffic": -8, "satisfaction": 2}, "Officers deployed. Traffic moves. Officers immediately redeployed elsewhere and it stops again."),
            Option("B. Announce odd-even plate expansion", "Rp 5 B", {"budget": -5, "traffic": -5, "bureaucracy": 6, "satisfaction": -4}, "New rule announced. Citizens buy second cars. Traffic neutral, revenue up, logic down."),
            Option("C. Study the jam", "Rp 10 B", {"budget": -10, "bureaucracy": 10, "feasibility_studies": 1}, "Consultants conclude the jam is caused by cars. Groundbreaking.", "The report costs more than the road it studies."),
            Option("D. Wait it out", "Rp 0 B", {"traffic": 8, "satisfaction": -6}, "The jam resolves itself after 9 hours. Two marriages end in the interim."),
        ],
    ),
    Event(
        "PUMP STATION HAS BROKEN DOWN.",
        "Pump Station No. 4 has stopped pumping. It has also stopped pretending.",
        [
            Option("A. Emergency repair", "Rp 40 B", {"budget": -40, "flood_risk": -12, "infrastructure": 3}, "Pump repaired by a man who is now too important to ever retire."),
            Option("B. Order replacement parts", "Rp 10 B", {"budget": -10, "flood_risk": 5, "bureaucracy": 5}, "Parts ordered. Estimated arrival: 14 business weeks.", "The parts arrive in month 3 of the next administration."),
            Option("C. Rent a temporary pump", "Rp 25 B", {"budget": -25, "flood_risk": -8}, "Temporary pump installed. It is still there. It is now permanent. Everything temporary is."),
            Option("D. Issue a statement", "Rp 1 B", {"budget": -1, "bureaucracy": 8, "satisfaction": -5, "flood_risk": 6}, "Statement: 'The pump situation is under control.' The pump disagrees."),
        ],
    ),
    Event(
        "THE DOCUMENT HAS DISAPPEARED.",
        "Tender Document No. 44-C is missing. It was on the desk. The desk was here. This is deeply concerning.",
        [
            Option("A. Search for document", "Rp 3 B", {"budget": -3, "documents_lost": 1}, "Document found.", "Unfortunately, it is the wrong document. The correct one remains lost. Forever, probably."),
            Option("B. Print a new copy", "Rp 8 B", {"budget": -8, "bureaucracy": 10}, "New copy printed. It now has two different version numbers and neither is wrong."),
            Option("C. Launch an internal investigation", "Rp 15 B", {"budget": -15, "bureaucracy": 20, "meetings": 2, "satisfaction": -2, "documents_lost": 1}, "Investigation launched. Three more documents go missing during the investigation."),
            Option("D. Pretend it never existed", "Rp 0 B", {"bureaucracy": 5, "project_progress": -3}, "Everyone agrees the document never existed. The tender it governed also never existed. Nobody asks further questions."),
        ],
    ),
    Event(
        "CONTRACTOR IS DELAYED. AGAIN.",
        "The contractor reports progress of 'almost finished'. This phrase has been in use since March.",
        [
            Option("A. Enforce penalty clause", "Rp 0 B", {"budget": 25, "infrastructure": -2, "project_progress": 3}, "Penalty enforced. Contractor pays. Contractor also slows down, creatively."),
            Option("B. Grant extension", "Rp 5 B", {"budget": -5, "bureaucracy": 8, "project_progress": -4}, "Extension granted: 'one more month'. The contractor is moved by your faith."),
            Option("C. Replace contractor", "Rp 60 B", {"budget": -60, "project_progress": -6, "infrastructure": 4}, "New contractor hired. Their first act is to request an extension."),
            Option("D. Accept reality", "Rp 0 B", {"project_progress": -2, "satisfaction": -3}, "Reality accepted. The project will finish when it finishes. Time is a construct."),
        ],
    ),
    Event(
        "BUDGET REVISION REQUESTED.",
        "The finance department has discovered that the numbers do not match the other numbers.",
        [
            Option("A. Approve revision", "Rp 5 B", {"budget": 60, "bureaucracy": 12}, "Budget revised. Somehow there is now more money. Nobody investigates how. Ever."),
            Option("B. Reject revision", "Rp 0 B", {"bureaucracy": -5, "satisfaction": -4, "budget": -20}, "Revision rejected. Departments respond by spending less carefully out of spite."),
            Option("C. Form a revision committee", "Rp 10 B", {"budget": -10, "bureaucracy": 18, "meetings": 3}, "Committee formed. The committee forms a sub-committee. The sub-committee schedules meetings."),
            Option("D. Lose the revision request", "Rp 0 B", {"documents_lost": 1, "bureaucracy": 6}, "The request is misplaced. The budget stays wrong. This is the most cost-effective option."),
        ],
    ),
    Event(
        "EMERGENCY MEETING CALLED.",
        "An emergency meeting has been called about the previous emergency meeting.",
        [
            Option("A. Attend personally", "Rp 2 B", {"budget": -2, "bureaucracy": 10, "meetings": 2}, "You attend. Four hours pass. One action item is produced. It is 'schedule follow-up meeting'."),
            Option("B. Send a representative", "Rp 5 B", {"budget": -5, "bureaucracy": 14, "meetings": 2}, "Your representative attends, takes notes, and forms a committee to review the notes."),
            Option("C. Decline, cite schedule conflict", "Rp 0 B", {"bureaucracy": -4, "satisfaction": -2}, "You decline. The meeting proceeds without you and makes three decisions about your departments."),
            Option("D. Reschedule indefinitely", "Rp 1 B", {"budget": -1, "bureaucracy": 6, "meetings": -1}, "Meeting postponed to 'next convenient date'. The date is never convenient. This is working as intended."),
        ],
    ),
    Event(
        "PUBLIC COMPLAINT RECEIVED.",
        "A citizen has written 47 pages about a pothole. It is well-researched. It has appendices.",
        [
            Option("A. Respond and fix the issue", "Rp 30 B", {"budget": -30, "satisfaction": 10, "infrastructure": 3}, "Pothole fixed. The citizen writes another 12 pages. This time with photographs."),
            Option("B. Send a form letter", "Rp 2 B", {"budget": -2, "bureaucracy": 8, "satisfaction": -6}, "Form letter sent: 'Thank you for your input.' The input is filed. The input stays filed."),
            Option("C. Invite citizen to a hearing", "Rp 8 B", {"budget": -8, "bureaucracy": 12, "meetings": 1, "satisfaction": 2}, "Hearing held. Citizen speaks for 90 minutes. The pothole is now better documented than the bridge."),
            Option("D. Ignore", "Rp 0 B", {"satisfaction": -8}, "Complaint ignored. Citizen escalates to social media. The pothole gains followers."),
        ],
    ),
    Event(
        "BRIDGE INSPECTION DUE.",
        "The old bridge requires its biennial inspection. The last inspection was nine years ago.",
        [
            Option("A. Full structural inspection", "Rp 35 B", {"budget": -35, "infrastructure": 5}, "Inspection complete. Bridge rated 'standing'. This is the second-highest available grade."),
            Option("B. Visual inspection from a car", "Rp 5 B", {"budget": -5, "bureaucracy": 5}, "Inspector drives over bridge at speed. Bridge does not collapse. Inspection passed.", "This methodology is now standard practice."),
            Option("C. Close bridge 'pending review'", "Rp 10 B", {"budget": -10, "traffic": 15, "satisfaction": -8, "bureaucracy": 6}, "Bridge closed. Traffic rerouted onto a bridge in worse condition. Risk redistributed evenly."),
            Option("D. Postpone to next year", "Rp 0 B", {"infrastructure": -4, "documents_lost": 1}, "Inspection postponed. The postponement letter itself is subsequently lost."),
        ],
    ),
    Event(
        "DRAINAGE BLOCKAGE REPORTED.",
        "Something is in the drainage. Several somethings. One may be a refrigerator.",
        [
            Option("A. Full drainage clearing operation", "Rp 45 B", {"budget": -45, "flood_risk": -14, "infrastructure": 4}, "Drainage cleared. Recovered items catalogued and, disturbingly, numbered."),
            Option("B. Send one worker with one stick", "Rp 3 B", {"budget": -3, "flood_risk": -3, "satisfaction": -2}, "Worker pokes blockage. Blockage relocates 200 meters downstream. Technically cleared."),
            Option("C. Commission drainage master plan", "Rp 20 B", {"budget": -20, "bureaucracy": 12, "feasibility_studies": 1, "flood_risk": 4}, "Master plan commissioned: 340 pages, 11 maps, 0 drains cleaned."),
            Option("D. Reroute the water", "Rp 0 B", {"flood_risk": 6, "satisfaction": -5}, "Water rerouted into neighboring district. Neighboring district reroutes it back. Water wins."),
        ],
    ),
    Event(
        "PROCUREMENT PROBLEM.",
        "The winning bid was submitted by a company that does not exist, for goods that also do not exist.",
        [
            Option("A. Cancel the tender", "Rp 5 B", {"budget": -5, "bureaucracy": 8, "project_progress": -3}, "Tender cancelled. New tender launched. Same bidders register under new names. Names are cheap."),
            Option("B. Proceed anyway", "Rp 50 B", {"budget": -50, "infrastructure": -2, "bureaucracy": 15, "documents_lost": 2}, "Contract signed. Goods do not arrive. Paperwork, however, arrives in abundance."),
            Option("C. Re-tender with new requirements", "Rp 15 B", {"budget": -15, "bureaucracy": 20, "meetings": 2, "feasibility_studies": 1}, "New requirements: bidders must now submit 44 documents, in triplicate, certified by a notary who is on leave."),
            Option("D. Quietly bury the file", "Rp 0 B", {"documents_lost": 1, "bureaucracy": 6}, "File buried in Archive Room B. Archive Room B is later converted into a meeting room."),
        ],
    ),
    Event(
        "CONSTRUCTION ACCIDENT AT SITE.",
        "An excavator has excavated something that was not on any map. The map is very old. The excavator is fine.",
        [
            Option("A. Halt work, full safety review", "Rp 25 B", {"budget": -25, "project_progress": -5, "satisfaction": 3, "infrastructure": 2}, "Site halted. Safety review finds 60 issues. 60 issues are logged. 3 are fixed."),
            Option("B. Fix and continue same day", "Rp 15 B", {"budget": -15, "project_progress": 4, "infrastructure": -2}, "Work continues. The schedule is honored. The schedule remains, as always, fictional."),
            Option("C. Blame the excavator operator", "Rp 0 B", {"satisfaction": -6, "bureaucracy": 5, "project_progress": -2}, "Operator blamed. Operator's cousin works at the newspaper. The newspaper is interested."),
            Option("D. Declare it an 'archaeological pause'", "Rp 5 B", {"budget": -5, "bureaucracy": 12, "project_progress": -6}, "Work paused indefinitely for 'cultural assessment'. The excavated object is a concrete block. Assessment continues."),
        ],
    ),
    Event(
        "A VERY IMPORTANT MEETING.",
        "You have been summoned to a Very Important Meeting. The agenda says 'AGENDA: TBD'. The dress code says 'mandatory'.",
        [
            Option("A. Attend with full preparation", "Rp 10 B", {"budget": -10, "bureaucracy": 12, "meetings": 1, "satisfaction": -2}, "You prepare a 30-slide deck. It is not needed. The meeting was about next month's meeting.", "Your deck is requested. Then lost."),
            Option("B. Attend, say nothing", "Rp 2 B", {"budget": -2, "bureaucracy": 8, "meetings": 1}, "You attend silently for 5 hours. You are assigned two action items. Nobody knows how this happened."),
            Option("C. Skip it", "Rp 0 B", {"bureaucracy": -3, "satisfaction": -3}, "You skip. The meeting concludes without you and cancels one of your projects. Which one is not specified."),
            Option("D. Schedule a conflicting meeting", "Rp 4 B", {"budget": -4, "bureaucracy": 16, "meetings": 2}, "You attend both meetings simultaneously via two phones. Both minutes list you as 'present but distracted'."),
        ],
    ),
    Event(
        "MEETING ABOUT THE PREVIOUS MEETING.",
        "Concerns were raised at the last meeting about how the last meeting was run. A meeting has been scheduled.",
        [
            Option("A. Attend and take minutes", "Rp 3 B", {"budget": -3, "bureaucracy": 18, "meetings": 2}, "Minutes taken. The minutes require a review meeting. The review meeting will have its own minutes.", "This sentence is load-bearing."),
            Option("B. Propose cancelling all meetings", "Rp 0 B", {"bureaucracy": -8, "meetings": -2, "satisfaction": 3}, "Proposal tabled. Tabling the proposal requires a meeting. Net meetings: unchanged. Entropy: increased."),
            Option("C. Send the Bureaucrat", "Rp 6 B", {"budget": -6, "bureaucracy": 22, "meetings": 3}, "The Bureaucrat thrives. The Bureaucrat proposes a standing weekly series. The series is approved by silence."),
            Option("D. Declare the previous meeting official retroactively", "Rp 1 B", {"budget": -1, "bureaucracy": 10, "documents_lost": 1}, "Minutes from the previous meeting are 'reconstructed'. Nobody can verify them, because the document is lost."),
        ],
    ),
    Event(
        "FLOOD CONTROL DIKE SHOWS SEEPAGE.",
        "Water is appearing where water should not appear. An engineer has used the word 'concerning' twice in one sentence.",
        [
            Option("A. Emergency dike reinforcement", "Rp 70 B", {"budget": -70, "flood_risk": -18, "infrastructure": 5}, "Dike reinforced. Flood risk drops. The engineer uses the word 'concerning' only once now."),
            Option("B. Install monitoring sensors", "Rp 20 B", {"budget": -20, "flood_risk": -5, "bureaucracy": 4}, "Sensors installed. You will now receive hourly reports of the water continuing to leak."),
            Option("C. Sandbags and hope", "Rp 10 B", {"budget": -10, "flood_risk": -6}, "Sandbags deployed. Hope, per the audit, is not a recognized engineering control."),
            Option("D. Relocate the warning sign", "Rp 1 B", {"budget": -1, "flood_risk": 8, "satisfaction": -4}, "Sign moved. Technically the seepage is now outside the warning zone. The water does not read signs."),
        ],
    ),
    Event(
        "CITY WINS AN AWARD.",
        "Against all evidence, the city has won a regional award for 'Administrative Resilience'.",
        [
            Option("A. Accept with ceremony", "Rp 15 B", {"budget": -15, "satisfaction": 8, "bureaucracy": 6, "meetings": 1}, "Ceremony held. Speeches given. The trophy is placed in a cabinet. The cabinet is later lost during an office move."),
            Option("B. Accept quietly, no press", "Rp 2 B", {"budget": -2, "satisfaction": 3}, "Award accepted quietly. This is, statistically, the wisest decision you will make all year."),
            Option("C. Frame the certificate in every office", "Rp 8 B", {"budget": -8, "bureaucracy": 10, "satisfaction": 4}, "Certificates framed city-wide. Productivity drops. Morale rises. Classic."),
            Option("D. Question the award's methodology", "Rp 0 B", {"bureaucracy": 5, "satisfaction": -3, "documents_lost": 1}, "You request the scoring methodology. The committee cannot locate it. Nobody can. The award was, perhaps, also lost."),
        ],
    ),
]


def generate_event(used: set) -> Event:
    """Pick an event that has not fired recently."""
    available = [i for i in range(len(EVENT_LIBRARY)) if i not in used]
    if not available:
        used.clear()
        available = list(range(len(EVENT_LIBRARY)))
    idx = random.choice(available)
    used.add(idx)
    return EVENT_LIBRARY[idx]
