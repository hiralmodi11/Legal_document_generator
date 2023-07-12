import streamlit as st
from legal_documents import generate_affidavit, generate_will, generate_power_of_attorney, generate_name_change_affidavit, generate_special_power_of_attorney, vakalatnama, generate_tenancy_lease


# Create the Streamlit app
def main():
  # Set the app title
  st.title("Legal Document Generator")

  # Document selection
  document_type = st.selectbox("Select the document type:", [
    "Affidavit", "Will", "Power of Attorney", "Vakalatnama", "Lease Agreement"
  ])

  if document_type == "Affidavit":
    # Affidavit subtype selection
    affidavit_subtype = st.selectbox(
      "Select the affidavit subtype:",
      ["Simple Affidavit", "Name Change Affidavit"])

    if affidavit_subtype == "Simple Affidavit":
      # Simple Affidavit inputs
      petitioner = st.text_area("Petitioner")
      respondent = st.text_area("Respondent")
      deponent_name = st.text_input("Deponent Name")

      # Generate the Simple Affidavit
      affidavit_content = generate_affidavit(petitioner, respondent,
                                             deponent_name)

      # Display the generated Simple Affidavit
      st.text_area("Simple Affidavit", value=affidavit_content, height=300)

    elif affidavit_subtype == "Name Change Affidavit":
      # Name Change Affidavit inputs
      deponent_name = st.text_area("Deponent")

      # Generate the Name Change Affidavit
      name_change_affidavit_content = generate_name_change_affidavit(
        deponent_name)

      # Display the generated Name Change Affidavit
      st.text_area("Name Change Affidavit",
                   value=name_change_affidavit_content,
                   height=300)

  elif document_type == "Will":
    # Will inputs
    testator_name = st.text_input("Testator Name")
    beneficiary_name = st.text_input("Beneficiary Name")
    executor = st.text_input("Executor")

    # Generate the Will
    will_content = generate_will(testator_name, beneficiary_name, executor)

    # Display the generated Will
    st.text_area("Will", value=will_content, height=300)

  elif document_type == "Power of Attorney":
    # Power of Attorney subtype selection
    poa_subtype = st.selectbox(
      "Select the power of attorney subtype:",
      ["General Power of Attorney", "Special Power of Attorney"])

    if poa_subtype == "General Power of Attorney":
      # General Power of Attorney inputs
      grantor_name = st.text_input("Grantor Name")
      agent_name = st.text_input("Agent Name")

      # Generate the General Power of Attorney
      power_of_attorney_content = generate_power_of_attorney(
        grantor_name, agent_name)

      # Display the generated General Power of Attorney
      st.text_area("General Power of Attorney",
                   value=power_of_attorney_content,
                   height=300)

    elif poa_subtype == "Special Power of Attorney":
      # Special Power of Attorney inputs
      grantor_name = st.text_input("Grantor Name")
      agent_name = st.text_input("Agent Name")

      # Generate the Special Power of Attorney
      special_power_of_attorney_content = generate_special_power_of_attorney(
        grantor_name, agent_name)

      # Display the generated Special Power of Attorney
      st.text_area("Special Power of Attorney",
                   value=special_power_of_attorney_content,
                   height=300)

  elif document_type == "Vakalatnama":
    lawyer_name = st.text_input("Lawyer Name")
    your_name = st.text_input("Your name")
    vakalatnama_content = vakalatnama(lawyer_name, your_name)
    st.text_area("Vakalatnama", value=vakalatnama_content, height=300)

  if document_type == "Lease Agreement":
    lessor = st.text_input("Lessor")
    lessee = st.text_input("Lessee")
    rent_amount = st.text_input("Rent Amount")
    duration = st.text_input("Duration")
    lease_content = generate_tenancy_lease(lessor, lessee, rent_amount,
                                           duration)
    st.text_area("Lease Agreement", value=lease_content, height=300)


# Run the app
if __name__ == "__main__":
  main()





