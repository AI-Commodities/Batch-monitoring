text
1025345679 ERROR

ERROR - <executing script 'TradeValidationFlow'> >
DB_ExecSql: OCIStmtExecute() for non queries failed
ORA-02291: integrity constraint (CEIOLFPROD.FK_TRADE_COUNTERPARTY) violated - parent key not found
ORA-06512: at line 256

Failed to execute OpenComponents/Java script 'com.citi.olf.trade.TradeValidationFlow' (34568):
Error: Exception occurred. Exception - Fatal Error: OCI Failure (2291)

Missing counterparty record: CP_ID = 'CITI_NA_56789' in COUNTERPARTY_MASTER table
text
1025345680 ERROR

ERROR - <executing script 'PriceUploadFlow'> >
DB_ExecSql: OCIStmtExecute() for non queries failed
ORA-01722: invalid number
ORA-06512: at line 89

Failed to execute OpenComponents/Java script 'com.citi.olf.pricing.PriceUploadFlow' (34569):
Error: Exception occurred. Exception - Fatal Error: OCI Failure (1722)

Invalid numeric value: field 'PRICE_AMOUNT' contains 'ABC.DEF' from row 47 of incoming feed file
text
1025345681 ERROR

ERROR - <executing script 'PositionReconciliationFlow'> >
DB_ExecSql: OCIStmtExecute() for non queries failed
ORA-00001: unique constraint (CEIOLFPROD.PK_POSITION_RECON_ID) violated
ORA-06512: at line 312

Failed to execute OpenComponents/Java script 'com.citi.olf.position.PositionReconciliationFlow' (34570):
Error: Exception occurred. Exception - Fatal Error: OCI Failure (1)

Duplicate position key: BOOK='NY_FIXED_INCOME', INSTRUMENT_ID='ISIN_US123456', DATE='2026-06-08'
text
1025345682 ERROR

ERROR - <executing script 'SettlementInstructionFlow'> >
DB_ExecSql: OCIStmtExecute() for non queries failed
ORA-01843: not a valid month
ORA-06512: at line 178

Failed to execute OpenComponents/Java script 'com.citi.olf.settlement.SettlementInstructionFlow' (34571):
Error: Exception occurred. Exception - Fatal Error: OCI Failure (1843)

Invalid date format: '2026-13-45' in SETTLEMENT_DATE column, feed file line 234
text
1025345683 ERROR

ERROR - <executing script 'ExposureCalcFlow'> >
DB_ExecSql: OCIStmtExecute() for non queries failed
ORA-00904: "NET_EXPOSURE_AMT": invalid identifier
ORA-06512: at line 445

Failed to execute OpenComponents/Java script 'com.citi.olf.exposure.ExposureCalcFlow' (34572):
Error: Exception occurred. Exception - Fatal Error: OCI Failure (904)

Column missing in table EXPOSURE_SUMMARY. Expected column 'NET_EXPOSURE_AMT' (typo or schema mismatch)
text
1025345684 ERROR

ERROR - <executing script 'AccountingPostingFlow'> >
DB_ExecSql: OCIStmtExecute() for non queries failed
ORA-01653: unable to extend table "CEIOLFPROD"."GL_TXN_DETAIL" by 64 in tablespace "TS_GL_DATA"
ORA-06512: at line 512

Failed to execute OpenComponents/Java script 'com.citi.olf.accounting.AccountingPostingFlow' (34573):
Error: Exception occurred. Exception - Fatal Error: OCI Failure (1653)

Tablespace TS_GL_DATA at 99.5% capacity. Autoextend disabled.
text
1025345685 ERROR

ERROR - <executing script 'RiskAggregationFlow'> >
DB_ExecSql: OCIStmtExecute() for non queries failed
ORA-03113: end-of-file on communication channel
ORA-06512: at line 623

Failed to execute OpenComponents/Java script 'com.citi.olf.risk.RiskAggregationFlow' (34574):
Error: Exception occurred. Exception - Fatal Error: OCI Failure (3113)

Database connection terminated during bulk fetch. Check network stability between ALM and Oracle RAC.
text
1025345686 ERROR

ERROR - <executing script 'ReportGenerationFlow'> >
DB_ExecSql: OCIStmtExecute() for non queries failed
ORA-30036: unable to extend segment by 8 in undo tablespace 'UNDOTBS1'
ORA-06512: at line 134

Failed to execute OpenComponents/Java script 'com.citi.olf.reports.ReportGenerationFlow' (34575):
Error: Exception occurred. Exception - Fatal Error: OCI Failure (30036)

Undo tablespace full. Long-running query exceeded undo retention period.
