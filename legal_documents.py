#affidavit
def generate_affidavit(petitioner, respondent, deponent_name):
  affidavit_content = f"""
    IN THE HONBLE HIGH COURT OF __________ AT __________
    
    WRIT PETITION NO. ____ OF 2000
    
    {petitioner}
    VERSUS
    {respondent}
    
    Affidavit of {deponent_name}, aged about ____ years, son of______, resident of ____________.
    
    I, the deponent above-named, do hereby solemnly affirm and state on oath as under:
    
    1. That I am the Petitioner in the aforesaid Writ Petition and am conversant with full facts of the case.
    
    2. That the deponent has read the Writ Petition and annexures, the contents of which he has fully understood.
    
    3. That the contents of paragraphs 1 to 20, of the Writ Petition are true to the own knowledge of the deponent.
    
    4. That annexures A to T to the Writ Petition have been compared and are certified to be true copies of their originals.
    
    DEPONENT
    
    I, the above-named deponent, do very that the contents of paragraphs 1 to 4 of this affidavit are true to my own knowledge. No part of it is false and nothing material has been concealed.

 

Verified at ____________, on this ___ day of _________, 2000. 



DEPONENT
"""
  return affidavit_content


def generate_name_change_affidavit(deponent_name):
  name_change_affidavit_content = f"""
  AFFIDAVIT FOR CHANGE OF NAME AFTER MARRIAGE [FEMALE]
  I, {deponent_name} daughter of ___________________________ and wife
  of ______________________________ aged _________, residing at
  _____________________________________________________________________________, do
  hereby solemnly affirm and declare as Under:
  1. That my maiden name is __________________________________________________.
  2. That I got married to [name of the husband] on [date of marriage] at [place of marriage] vide
  marriage certificate having number _______________ dated ___________, issued by _______.
  3. After marriage my name is ________________________________________ .
  4. That in my marriage certificate both the names of mine and name of my husband are stated.
  5. That my AADHAR number is ____________________ which is same before and after marriage.
  6. That my PAN number is __________________________ which is same before and after marriage.
  7. That the said expanded initial (Name), namely ,may kindly be treated as first name
  _ , may be treated asmiddlename, _ as the last name.
  8. I state that [maiden name] and the [present name] is the name of one and the same person and that
  is myself.
  I am executing this declaration to be submitted to the concerned authorities for the change of my name
  in membership database.
  I hereby state that whatever is stated herein above are true to the best of my Knowledge.
  ____[Signature of Deponent]______               ________Date_________
  (Affix Passport Size Photograph)
  
  Witness
  1)
  2)
  
  NOTES:
  1. The affidavit has to be sworn before a Notary Public.
  2.The photograph of the Deponent should be pasted on the affidavit and attested by the Notary Public
  with his/her signature and rubber stamps.
  3. Copy of Aadhar card, PAN card, Marriage Certificate to be attached. 
  
  """
  return name_change_affidavit_content


#Will
def generate_will(testator_name, beneficiary_name, executor):
  will_content = f"""
I {testator_name}, son/daughter of Shri _______________, aged ___ years, resident of ______________________________, do hereby revoke all my former Wills, Codicils and Testamentary dispositions made by me. I declare this to be my last Will and Testament. 

I maintain good health, and possess a sound mind. This Will is made by me of my own independent decision and free volition. Have not be influenced, cajoled or coerced in any manner whatsoever. 

I hereby appoint my {executor}, as the sole Executor of this WILL.

I own following immovable and movable assets. 

One Flat No.___ in _______________________.

Jewelry, ornaments, cash, National Saving Certificate, Public Provident Fund, shares in various companies, cash in hand and also with certain banks. 

All the assets owned by me are self-acquired properties. No one else has any right, title, interest, claim or demand whatsoever on these assets or properties. I have full right, absolute power and complete authority on these assets, or in any other property which may be substituted in their place or places which may be Acquired or received by me hereafter.

I hereby give, devise and bequeath all my properties, whether movable or immovable, whatsoever and wheresoever to {beneficiary_name} absolutely forever.

IN WITNESS WHEREOF I have hereunto set my hands on this ____ day of ____, 2000 at ____________. 


-sd-
TESTATRIX

SIGNED by the abovenamed Testatrix  as his last WILL and Testament in our presence, who appear to have perfectly understood & approved the contents in the presence of both of us presents, at the same time who in his presence and in the presence of each other have hereunto subscribed our names as Witnesses.                                      

WITNESSES :

1.


2.

"""
  return will_content


#


def generate_power_of_attorney(grantor_name, agent_name):
  power_of_attorney_content = f"""
TO ALL TO WHOM THESE PRESENTS SHALL COME
Know all men by these presents that I {grantor_name} s/d/o __________ aged ___ yrs resident of _________________, state as follows :-
Whereas I am personally unable to attend to the managerial and other affairs with respect to my property, so I, hereby nominate and appoint Shri/Smt {agent_name} R/o……………… as my true and lawful Attorney to act for and on my behalf and I authorize and empower him to do the following acts, deeds and things on my behalf:-
1. To rent the aforementioned property by leave and license agreement.
2. To purchase the stamp, make, sign, execute and admit the execution of leave and license agreement and to appear before the sub registrar for the registration of the leave and license agreement of the aforesaid property.
3. To demand, collect the rent due on the aforementioned property.
4. To manage and control my aforesaid property including collection of monthly rents, from the licensees and issuance of proper stamped receipts acknowledging the rent received. 
5. To make applications, affidavits, documents etc., to the Govt. Departments and any other concerned authorities, required for the managing of the aforesaid property and to do all other acts, deeds and things in respect thereof.
6. To effect and carry out necessary repairs, additions, etc., in the said property as and when may be desired, and for this purpose obtain all the necessary permissions and/or sanctions, necessary from any appropriate authority.
7. To deal with Govt. departments and other local bodies for the purpose of any essential facilities or amenities required to be provided in the building. He can sign all papers and documents etc. for this purpose.
8. To pay all the taxes, Municipal levies and other taxes, which may be, required to be paid. 
9. To file any objections with Govt. departments or other local body of Government for any purpose related with said property. 
10.To furnish the details of Licensee to concerned Police Station, to get No Objection from the local Police by appearing personally as and when required or called by the Police of concerned jurisdiction.
11.To pay maintenance charges to society and attend society meetings.
12.To engage any Advocate or Attorney for the purpose and or to appear for and represent our in all the courts, civil, criminal or revenue including labour tribunals, original, revisional or appellate, in any registration offices, and also to present appeals in any court, and also to accept services of all summons, notices and other processes of law.
13.AND GENERALLY TO DO ALL other acts, deeds and things, which my 
said attorneys may deem fit and proper for the maintenance, upkeep of my 
property.
14.This power of attorney is without any consideration.


Provided that the said attorney shall not sell or transfer the ownership of the property to any person. Provided further that the said attorney shall keep true accounts of all activities performed by virtue of this power of attorney.

                      AND


I hereby agree and undertake to confirm and ratify all and whatsoever my said attorney shall do or purport to do by the virtue of this power of attorney. 

IN WITNESS WHERE OF this deed is signed by me at ________on this 
______day of_______ 

1. EXECUTANT 
Name & Signature - 


2. ATTORNEY HOLDER
“I hereby accept all the powers.”
Name & Signature - 
 
WITNESSES:
1. 

2. 
  
"""
  return power_of_attorney_content


def generate_special_power_of_attorney(grantor_name, agent_name):
  special_power_of_attorney_content = f"""
         SPECIAL POWER OF ATTORNEY TO EXECUTE THE SALE DEED AND PRESENT IT FOR REGISTRATION 

KNOW ALL MEN BY THESE PRESENTS that I,{grantor_name}, S/o ______, R/o __________, send GREETINGS 

WHEREAS presently I am residing at ______ and I intend to sell my property at _____(details regarding location, measurement etc. of the property) 
AND WHEREAS it is not convenient for me to visit _____ time and again for the formalities related with the sale. 
I, do hereby nominate, constitute and appoint {agent_name}, S/o ______, R/o __________, to be my true and lawful attorney for me and in my name on my behalf to do or cause to be done all or any of the following acts, deeds, matters and things that is to say:
1. To negotiate, sell and execute the sale deed and necessary forms 
and papers relating to the execution of the sale of the property more 
fully described above. 
2. To declare the value of the above property before the Sub-Registrar 
for purposes of registration of the sale deed. 
3. To appear before the Sub-Registrar of district and to present for 
registration the deed, to admit the execution thereof to do any act 
that may be necessary for the registration of the said document and 
to receive it back when it has been duly registered and to sign and 
deliver a proper receipt for the same. 
AND I hereby agree that all acts, deeds and things lawfully done by 
my said attorney shall be construed as acts, deeds and things done by 
me and I undertake to ratify and confirm all and whatsoever that my 
said attorney shall lawfully do or cause to be done for me by virtue of 
the power hereby given. 
IN WITNESS WHERE OF, I have signed this deed on this day of 
____________. 
Signed and delivered by the above named 
WITNESS: 
1. 
2.  

"""
  return special_power_of_attorney_content


def vakalatnama(your_name, lawyer_name):
  vakalatnama_content = f"""
Vakalatnama
  
Before the Honourable ………………………………………………..
  Between …………………………………………………….                   Petitioner /Applicant /
                                                  Appellant / Plaintiff
  
                    Vs.
  And     …………………………………………………….
  
                                            Respondent / Non-applicant
                                                    / Defendant
  I / we {your_name} do hereby appoint & retain {lawyer_name} (hereinafter called as “the Advocates”) to be my / our advocates in the said
  Suit /Appeal / Petition / Case /Reference / Revision / Execution. I / we authorize the Advocates to do any or all of the following on my / our behalf:
  a) to represent, act and appear for me / us;
  b) to conduct and prosecute (or defend) the same and all proceedings that may be taken in respect of any application connected with the same or any decree of order passed therein;
  c) to sign, file, verify, present, and receive all types of documents including plaints, statements, pleadings, appeals, cross objections, petitions, applications, revision, withdrawal, compromise or affidavits;
  d) to withdraw or compromise or submit to arbitration any differences or disputes that may arise touching or in any manner relating to the said case;
  e) to deposit, draw and receive money, cheques, cash and grant receipts thereof;
  f) to do all other acts and things which may be necessary or expedient, in the opinion of the Advocate, to be done.
  I/We do hereby agree to ratify and confirm all acts done by the Advocate or their substitute in the matter as my/our own acts, as if done by me/us to all intents and purposes.
  …………………………………………………………………
  Signatures of Persons Appointing the Advocates
  
  Advocate Name   Enrollment No.   Mobile No.    Signature of Advocate
  
  Date …………………………………
  Place ………………………………… 
    """
  return vakalatnama_content


def generate_tenancy_lease(lessor, lessee, rent_amount, duration):
  lease_content = f"""
               LEASE OF A HOUSE ON MONTHLY TENANCY
 

THIS AGREEMENT OF LEASE is entered into on _______ between {lessor}  s/d of ___________ r/o ___________ (hereinafter addressed as the lessor) and {lessee} s/d of ___________ r/o__________ (hereinafter addressed as the lessee).

BOTH THE LESSOR AND THE LESSEE AGREE ON THE FOLLOWING TERMS AND CONDITIONS OF THIS AGREEMENT OF LEASE:

1. That the lessor is the owner and landlord of House No._______ situated in ________, which he has agreed to let to the lessee at the rent of Rs.{rent_amount} Per month to the lessor, payable on the first day of each month in advance. The lessee agrees to take the aforesaid house on lease at the aforesaid rent rate.

2. That the lease is to commence with effect from ________, and the duration of the lease shall be {duration} from the date of its commencement.

3. That the lessee shall be responsible for keeping the leased premise in good shape. He shall keep all the fixtures, electric fittings and water connection in good running condition. However, the lessor reserves for himself the right to inspect the premises at all reasonable times and shall have the premises whitewashed and effect the substantial repairs.

4. That the lessee shall use the premises exclusively for residential purposes and shall not sublet the premises without the written permission of the lessor.

5. That the lessee shall pay the water tax and electricity charges in respect of the leased premises to the lessor in addition to the payment of rent as aforesaid. 

6. That the lessee shall deliver the peaceful vacant possession of the premises to the lessor at the termination of the lease period. Lessee intending to vacate the premises at an earlier date shall give a notice of his intention to the lessor to vacate the premises at the expiry of the period mentioned in the notice.

IN WITNESS WHEREOF the lessor and the lessee have signed this deed on the day and year first above written.
  

Signed by 

__________    ___________

(The lessor) (The lessor)

In Presence of 

1.

2. 
  """
  return lease_content
