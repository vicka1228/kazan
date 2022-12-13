import React from "react";
import { useParams } from "react-router-dom";
import { Sidebar } from "../components/molecules/Sidebar";
import styles from "./page_style.module.css";
import { useEffect, useState } from "react";
import axios from "axios";

export const ConcertPage = ({}) => {
  const { id } = useParams();

  //Concert Info API

  const [getConcertInfo, setGetConcertInfo] = useState({});
  let venue = id; //have to accept from user
  let req = {
    venue: venue,
  };
  useEffect(() => {
    axios
      .post("http://127.0.0.1:5000/flask/concertinfo", req)
      .then((response) => {
        console.log("SUCCESS", response);
        setGetConcertInfo(response);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);
  return (
    <>
      <Sidebar />
      <div className={styles.concert_page}>
        <div className={styles.concert_banner}>
          <img src="https://connorgroup.com/static/4bb1b295ecca0123d20cd18be8066649/cd40e/Concerts_near_San_Antonio-scaled.jpg"></img>
          <div>
            <p>The The Weeknd: After Hours til Dawn Tour</p>
            <p>Sat, 10 Jun 2023, 16:00 | Etihad Stadium, Manchester</p>
          </div>
        </div>
        <div className={styles.concert_info}>
          <div>
            <h2>Overview</h2>
            No persons under 5 permitted. Persons aged between 5-15 years old
            must be accompanied by an adult 21 or over (1 adult minimum per 4
            persons aged between 5-15 years old). You must bring valid and
            current ID with you - Valid IDs must be photographic. We will be
            accepting the following types of ID for entry into the event:
            Current UK or Overseas Driving License/ Provisional License
            Photocard Current UK or Overseas Current Passport Overseas Only
            Valid National ID card UK only 18 + PASS scheme card Young Scot
            Cards Ireland Age Card Forces ID Card This is line with the national
            Challenge 25 policy. **Photocopies of ID does not count as valid ID.
            Must be original documents A max of 4 tickets per person and per
            household applies for the presales, rising to 6 tickets per person
            and per household for the general sale. Tickets in excess of this
            will be cancelled. Event Info General Admission Only Ticket limit -
            4 on presale / 6 on general sale. Age restrictions - No persons
            under 5 permitted. Persons aged between 5-15 years old must be
            accompanied by an adult 21 or over (1 adult minimum per 4 persons
            aged between 5-15 years old). Resale restrictions - Tickets must not
            be purchased with the intention of reselling them. If you can no
            longer use your tickets, you may only resell them through authorised
            resale sites (Ticketmaster Fan to Fan Exchange). You may not resell
            or offer to resell tickets for this event through any unauthorised
            resale site. Any tickets purchased, resold or offered for resale in
            breach of these special conditions may be cancelled. Full terms can
            be found here(Opens in new tab) Lineup Guns N' Roses Ticket Limits A
            max of 4 tickets per person and per household applies for the
            presales, rising to 6 tickets per person and per household for the
            general sale. Tickets in excess of this will be cancelled. Please
            adhere to published ticket limits. Persons who exceed the ticket
            limit may have any or all of their orders and tickets cancelled
            without notice by Ticketmaster at its discretion. This includes
            orders associated with the same name, e-mail address, billing
            address, credit card number or other information. Prices are in GBP
          </div>
          <div className={styles.concert_prices}>
            <h2>Prices</h2>
            <div>
              Predicted price: 100$ <br />
              Minimum: 50$ <br />
              Maximum: 150$
            </div>
          </div>
        </div>
      </div>
    </>
  );
};
