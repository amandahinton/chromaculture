import React from 'react';
import './nav.css';

function Footer() {
  return (
    <div className="footer-div">
      <p className="footer-links">
        Chromaculture was built and is maintained by:
       <a className="footer-link" href={"https://amandahinton.com/"} target={"_blank"} rel={"noreferrer"}> Amanda Hinton</a>
      </p>
      <p className="footer-copyright">Copyright ©2021 All Rights Reserved.</p>
    </div>
  );
};

export default Footer;
