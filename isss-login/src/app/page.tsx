'use client'

import Image from "next/image";
import { FormEvent } from "react";


const reasons = [
  "I-20/DS-2019 Pick-Up",
  "Employment (OPT, CPT, AT, etc.)",
  "Appt. and Office Hours",
  "New Check-In",
  "Travel Signature",
  "I-20/DS-2019 Update (shorten, extend, major change, etc.)",
  "Transfer",
  "General (SSN, status letters, address, etc.)",
  "Change of Status",
  "Change of Level",
  "Dependent I-20",
  "Leave of Absence",
  "Reduced Course Load",
  "I-20/DS-2019 Reprint",
];


const Index = () => {

  async function handleClick(event: FormEvent<HTMLFormElement>){
    // event.preventDefault();
    const formValues:{ [key: string]: FormDataEntryValue } = {}
    const formData = new FormData(event.currentTarget)
    formData.entries().forEach(entry => {
      formValues[entry[0]] = entry[1];
    });
    const body = JSON.stringify(formValues)
    // console.log(body)
    try {
      const response = await fetch("http://localhost:3001/insert", {
        method: "POST",
        // mode:'no-cors',
        headers: {
          "Content-Type": "application/json",
        },
        body: body,
      });

      const data = await response.json();
      console.log(data)
      if (data.success) {
        alert("Form submitted successfully:");
      } else {
        console.error("Error submitting form:", data.error);
      }
    } catch (error) {
      console.error("Error submitting form:", error);
    }
  }
  return (
    <div className="p-4 flex gap-4 flex-col md:flex-row h-screen">
      {/* LEFT */}
      <div className="w-full lg:w-1/3 flex flex-col justify-center items-center gap-8 h-full">
        <Image src="/logo.png" alt="logo" width={200} height={200} />
        <span className="hidden text-center lg:block w-max font-bold">
          Stevens Institute of Technology
          <br />
          ISSS Login
        </span>
      </div>
      {/* RIGHT */}
      <div className="w-full lg:w-2/3 flex flex-col gap-8 bg-stevensRed p-8 overflow-y-auto h-full">
        <form onSubmit={handleClick} method="post">
          <div className="space-y-12">
            <div className="border-b border-gray-900/10 pb-12">
              <h2 className="text-base text-lg font-semibold leading-7 text-gray-900">
                Personal Information
              </h2>

              <div className="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
                <div className="sm:col-span-3">
                  <label
                    htmlFor="firstName"
                    className="block text-md font-medium leading-6 text-gray-900"
                  >
                    First name
                  </label>
                  <div className="mt-2">
                    <input
                      id="firstName"
                      name="firstName"
                      type="text"
                      autoComplete="givenName"
                      required
                      className="block w-full rounded-md border-0 p-4 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                    />
                  </div>
                </div>

                <div className="sm:col-span-3">
                  <label
                    htmlFor="lastName"
                    className="block text-md font-medium leading-6 text-gray-900"
                  >
                    Last name
                  </label>
                  <div className="mt-2">
                    <input
                      id="lastName"
                      name="lastName"
                      type="text"
                      autoComplete="familyName"
                      required
                      className="block w-full rounded-md border-0 p-4 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                    />
                  </div>
                </div>

                <div className="sm:col-span-3">
                  <label
                    htmlFor="cwid"
                    className="block text-md font-medium leading-6 text-gray-900"
                  >
                    Stevens CWID
                  </label>
                  <div className="mt-2">
                    <input
                      id="cwid"
                      name="cwid"
                      type="text"
                      autoComplete="family-name"
                      required
                      className="block w-full rounded-md border-0 p-4 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                    />
                  </div>
                </div>

                <div className="sm:col-span-3">
                  <label
                    htmlFor="email"
                    className="block text-sm font-medium leading-6 text-gray-900"
                  >
                    Email Address
                  </label>
                  <div className="mt-2">
                    <input
                      id="email"
                      name="email"
                      type="email"
                      autoComplete="email"
                      required
                      className="block w-full rounded-md border-0 p-4 py-1.5 text-gray-900 shadow-md ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                    />
                  </div>
                </div>
              </div>
            </div>

            <div className="border-b border-gray-900/10 pb-12">
              <div className="mt-10 space-y-10">
                <fieldset>
                  <legend className="text-lg font-semibold leading-6 text-gray-900">
                    Reason for Visit
                  </legend>
                  <div className="mt-6 grid grid-cols-1 md:grid-cols-2 gap-6">
                    {reasons.map((reason, index) => (
                      <div key={index} className="flex items-center gap-x-3">
                        <input
                          id={`reason-${index}`}
                          name="reason"
                          type="radio"
                          value={reason}
                          required
                          className="h-4 w-4 border-gray-300 text-indigo-600 focus:ring-indigo-600"
                        />
                        <label
                          htmlFor={`reason-${index}`}
                          className="block text-md font-medium leading-6 text-gray-900"
                        >
                          {reason}
                        </label>
                      </div>
                    ))}
                  </div>
                </fieldset>
              </div>
            </div>
          </div>

          <div className="mt-6 flex items-center justify-end gap-x-6">
            <button
              type="submit"
              className="rounded-md bg-white px-3 py-2 text-sm font-semibold text-black shadow-sm hover:bg-gray-200 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-black"
            >
              Submit
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default Index;


