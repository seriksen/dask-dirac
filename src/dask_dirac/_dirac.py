"""Module for HTTP DIRAC queries"""
from __future__ import annotations

from typing import Any

import requests


def _query(url: str, params: dict[str, str], capath: str, user_proxy: str) -> Any:
    if not capath:
        capath = "/etc/grid-security/certificates"
    if not user_proxy:
        user_proxy = (
            "/tmp/x509up_u1000"  # TODO: default path should be /tmp/x509up_u<user id>
        )
    with requests.post(
        url, data=params, cert=user_proxy, verify=capath, timeout=60
    ) as result:
        return result.json()


def submit_job(server_url: str, jdl: str, capath: str, user_proxy: str) -> Any:
    """Submit a job to a DIRAC server"""
    endpoint = "WorkloadManagement/JobManager"
    url = f"{server_url}/{endpoint}"
    params = {"method": "submitJob", "jobDesc": jdl}
    return _query(url, params, capath, user_proxy)


def get_jobs(server_url: str, capath: str, user_proxy: str) -> Any:
    """Get jobs from DIRAC server"""
    endpoint = "WorkloadManagement/JobMonitoring"
    url = f"{server_url}/{endpoint}"
    params = {"method": "getJobs"}
    return _query(url, params, capath, user_proxy)


def get_max_parametric_jobs(server_url: str, capath: str, user_proxy: str) -> Any:
    """Get max parametric jobs from DIRAC server (mostly for testing)"""
    endpoint = "WorkloadManagement/JobManager"
    url = f"{server_url}/{endpoint}"
    params = {"method": "getMaxParametricJobs"}
    return _query(url, params, capath, user_proxy)


def whoami(server_url: str, capath: str, user_proxy: str) -> Any:
    """Get user info from DIRAC server (mostly for testing)"""
    endpoint = "DataManagement/FileCatalog"
    url = f"{server_url}/{endpoint}"
    params = {"method": "whoami"}
    return _query(url, params, capath, user_proxy)